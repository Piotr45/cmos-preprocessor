import os
from typing import List, Tuple

import numpy as np
import pandas as pd
import wfdb
from numpy.typing import ArrayLike


def _list_all_people(dir: str) -> List[str]:
    return os.listdir(dir)


def _list_records_for_person(person_dir: str) -> List[str]:
    all_person_files = os.listdir(person_dir)
    record_names = list(set([file.split(".")[0] for file in all_person_files]))

    return record_names


def _read_record_and_annotation(
    person_dir: str, record_name: str
) -> Tuple[wfdb.Record, wfdb.Annotation]:
    if person_dir[-1] != "/":
        person_dir += "/"
    record = wfdb.rdrecord(f"{person_dir}{record_name}")
    annotation = wfdb.rdann(f"{person_dir}{record_name}", extension="atr")

    return (record, annotation)


def _prepare_record_data(
    record: wfdb.Record, annotation: wfdb.Annotation
) -> Tuple[ArrayLike, ArrayLike]:
    selected_channel = 1 if record.p_signal.shape[1] == 2 else 0
    ann_points = annotation.sample
    heartbeat_moments = ann_points.reshape(-1, 2)
    last_point = int(np.ceil(np.max(ann_points) / 100) * 100)
    ecg_data = record.p_signal[:last_point, selected_channel]
    mask = np.zeros(last_point, dtype="int8")

    for (heart_beat_start, heart_beat_end) in heartbeat_moments:
        mask[heart_beat_start:heart_beat_end] = 1

    return (ecg_data, mask)


def _make_training_sample(
    ecg_sample: ArrayLike, mask_sample: ArrayLike, sample_freq: int
) -> Tuple[ArrayLike, int]:
    sampled_points = np.linspace(0, ecg_sample.shape[0] - 1, sample_freq, dtype="int")
    response = 1 if 1 in mask_sample else 0

    return (ecg_sample[sampled_points], response)


def _make_training_samples(
    ecg_data: ArrayLike, mask: ArrayLike, sample_length: int, sample_freq: int
) -> Tuple[ArrayLike, ArrayLike]:
    sample_idx = np.arange(0, ecg_data.shape[0], sample_length)
    sample_windows = list(zip(sample_idx, sample_idx[1:]))

    samples_x = np.zeros(shape=(len(sample_windows), sample_freq))
    samples_y = np.zeros(shape=(len(sample_windows)))

    for i, (sample_start, sample_end) in enumerate(sample_windows):
        ecg_sample = ecg_data[sample_start:sample_end]
        mask_sample = mask[sample_start:sample_end]

        sample_x, sample_y = _make_training_sample(ecg_sample, mask_sample, sample_freq)
        samples_x[i] = sample_x
        samples_y[i] = sample_y

    return (samples_x, samples_y)


def _make_pandas_sample(samples_x: ArrayLike, samples_y: ArrayLike) -> ArrayLike:
    return np.hstack((samples_x, samples_y.reshape(-1, 1)))


def _make_pandas_samples(samples: List[Tuple[ArrayLike, ArrayLike]]) -> pd.DataFrame:
    pandas_samples = [
        _make_pandas_sample(sample_x, sample_y) for (sample_x, sample_y) in samples
    ]
    combined_pandas_samples = np.vstack(pandas_samples)
    return pd.DataFrame(data=combined_pandas_samples)
