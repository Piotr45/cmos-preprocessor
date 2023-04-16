import argparse
import os
import sys
from typing import List, Tuple

import numpy as np
import pandas as pd
import wfdb
from numpy.typing import ArrayLike


def parse_arguments(argv: List[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    arg_parser.add_argument(
        "--ds-dir",
        type=str,
        action="store",
        required=True,
        help="Directory with ECG data from physionet",
    )

    arg_parser.add_argument(
        "--output-file",
        type=str,
        action="store",
        required=True,
        help="File in which the dataset will be saved",
    )

    arg_parser.add_argument(
        "--sample-length",
        type=int,
        action="store",
        required=True,
        help="The length of a sample's window",
    )

    arg_parser.add_argument(
        "--sample-freq",
        type=int,
        action="store",
        required=True,
        help="Number of sampled points from a window",
    )

    arg_parser.add_argument(
        "--download",
        action="store_true",
        help="Whether to download database or not",
    )

    return arg_parser.parse_args(argv)


def _list_all_people(dir: str) -> List[str]:
    """List all people within  a dataset

    Args:
        dir (str): directory containing raw data from physionet

    Returns:
        List[str]: list of people
    """
    return os.listdir(dir)


def _list_records_for_person(person_dir: str) -> List[str]:
    """List all record names for a given person

    Args:
        person_dir (str): directory containing records of a given person

    Returns:
        List[str]: record names
    """
    all_person_files = os.listdir(person_dir)
    record_names = list(
        set([file.split(".")[0] for file in all_person_files])
    )  # a person's directory contains data files, header files etc which duplicate records' names

    return record_names


def _read_record_and_annotation(
    person_dir: str, record_name: str
) -> Tuple[wfdb.Record, wfdb.Annotation]:
    """Read record's data and annotation of a given record for a given person

    Args:
        person_dir (str): directory containing records of a given person
        record_name (str): record name

    Returns:
        Tuple[wfdb.Record, wfdb.Annotation]: tuple of record's data and annotation
    """
    if person_dir[-1] != "/":
        person_dir += "/"
    record = wfdb.rdrecord(f"{person_dir}{record_name}")
    annotation = wfdb.rdann(f"{person_dir}{record_name}", extension="atr")

    return record, annotation


def _prepare_record_data(
    record: wfdb.Record, annotation: wfdb.Annotation
) -> Tuple[ArrayLike, ArrayLike]:
    """Prepare record data - keep only the data for which annotations are available,
    create a binary mask

    Args:
        record (wfdb.Record): record
        annotation (wfdb.Annotation): annotation

    Returns:
        Tuple[ArrayLike, ArrayLike]: tuple of ecg signals and a binary mask
    """
    selected_channel = (
        1 if record.p_signal.shape[1] == 2 else 0
    )  # select the filtered signal if possible
    ann_points = annotation.sample
    heartbeat_moments = ann_points.reshape(
        -1, 2
    )  # create (beginning, end) pairs of heartbeat points
    last_point = int(
        np.ceil(np.max(ann_points) / 100) * 100
    )  # find the last point for which an annotation is available and round
    ecg_data = record.p_signal[
        :last_point, selected_channel
    ]  # remove the data without annotations
    mask = np.zeros(last_point, dtype="int8")  # initialize a binary mask

    for (
        heart_beat_start,
        heart_beat_end,
    ) in heartbeat_moments:  # mark heartbeat moments on a mask
        mask[heart_beat_start:heart_beat_end] = 1

    return ecg_data, mask


def _make_training_sample(
    ecg_sample: ArrayLike, mask_sample: ArrayLike, sample_freq: int
) -> Tuple[ArrayLike, int]:
    """Create a vector of length `sample_freq` and corresponding responses.
    A response is 1 if any value of `mask_sample` is 1. Works on a sample's window

    Args:
        ecg_sample (ArrayLike): ecg signal window
        mask_sample (ArrayLike): binary mask window
        sample_freq (int): number of points sampled from an ecg signal window

    Returns:
        Tuple[ArrayLike, int]: tuple of a vector of length `sample_freq`
        and corresponding response
    """
    sampled_points = np.linspace(
        0, ecg_sample.shape[0] - 1, sample_freq, dtype="int"
    )  # draw `sample_freq` equally spaced points
    response = (
        1 if np.mean(mask_sample) > 0.4 else 0
    )  # determine a response based on the mask

    return ecg_sample[sampled_points], response


def _make_training_samples(
    ecg_data: ArrayLike, mask: ArrayLike, sample_length: int, sample_freq: int
) -> Tuple[ArrayLike, ArrayLike]:
    """Apply `_make_training_sample` on a whole record (on all sample windows)

    Args:
        ecg_data (ArrayLike): ecg signal data of a record
        mask (ArrayLike): binary mask of a record
        sample_length (int): length of a sample's window
        sample_freq (int): number of points in each window

    Returns:
        Tuple[ArrayLike, ArrayLike]: tuple of vectors of length `sample_freq`
        and corresponding responses
    """
    sample_idx = np.arange(
        0, ecg_data.shape[0], sample_length
    )  # split whole signal data into parts
    sample_windows = list(
        zip(sample_idx, sample_idx[1:])
    )  # create sample windows of length `sample_length`

    samples_x = np.zeros(shape=(len(sample_windows), sample_freq))
    samples_y = np.zeros(shape=(len(sample_windows)))

    for i, (sample_start, sample_end) in enumerate(sample_windows):
        ecg_sample = ecg_data[sample_start:sample_end]
        mask_sample = mask[sample_start:sample_end]

        sample_x, sample_y = _make_training_sample(
            ecg_sample, mask_sample, sample_freq
        )
        samples_x[i] = sample_x
        samples_y[i] = sample_y

    return samples_x, samples_y


def _make_pandas_sample(
    samples_x: ArrayLike, samples_y: ArrayLike
) -> ArrayLike:
    """Transform training samples into tabular format - the last field are the responses

    Args:
        samples_x (ArrayLike): ecg sampled signals
        samples_y (ArrayLike): responses

    Returns:
        ArrayLike: vector containing ecg sampled signal data and responses,
        i.e [sig1, sig2, sig3, ..., sig_n, response]
    """
    return np.hstack((samples_x, samples_y.reshape(-1, 1)))


def _make_pandas_samples(
    samples: List[Tuple[ArrayLike, ArrayLike]]
) -> pd.DataFrame:
    """Apply `_make_pandas_sample` on all samples

    Args:
        samples (List[Tuple[ArrayLike, ArrayLike]]): list containing ecg signal windows
        and responses of all records

    Returns:
        pd.DataFrame: final dataset, each row contains sampled signal values
        and a corresponding response
    """
    pandas_samples = [
        _make_pandas_sample(sample_x, sample_y)
        for (sample_x, sample_y) in samples
    ]
    combined_pandas_samples = np.vstack(pandas_samples)
    return pd.DataFrame(data=combined_pandas_samples)


def main() -> None:
    # parse arguments
    args = parse_arguments(sys.argv[1:])
    ds_dir = args.ds_dir

    output_file = args.output_file
    sample_length = args.sample_length
    sample_freq = args.sample_freq
    download = args.download

    # standardize the datasource path
    if ds_dir[-1] != "/":
        ds_dir += "/"

    # create a datasource directory if doesn't exist
    if not os.path.isdir(ds_dir):
        os.mkdir(ds_dir)

    # download physionet data
    if download:
        wfdb.dl_database("ecgiddb", ds_dir)

    all_people = _list_all_people(ds_dir)
    people_record_names = [
        _list_records_for_person(f"{ds_dir}{person_name}")
        for person_name in all_people
    ]
    people_records_and_annotations = [
        _read_record_and_annotation(f"{ds_dir}{person_name}", rec_name)
        for i, person_name in enumerate(all_people)
        for rec_name in people_record_names[i]
    ]
    prepared_people_data = [
        _prepare_record_data(rec, ann)
        for (rec, ann) in people_records_and_annotations
    ]
    samples = [
        _make_training_samples(ecg_data, mask, sample_length, sample_freq)
        for (ecg_data, mask) in prepared_people_data
    ]
    pandas_samples = _make_pandas_samples(samples)

    pandas_samples.to_csv(output_file, index=None)


if __name__ == "__main__":
    main()
