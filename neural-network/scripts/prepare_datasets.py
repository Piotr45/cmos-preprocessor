from pathlib import Path
from typing import Optional, Union

import numpy as np
import pandas as pd
import wfdb

from prepare_dataset import (
    _list_all_people,
    _list_records_for_person,
    _make_pandas_samples,
    _make_training_samples,
    _prepare_record_data,
    _read_record_and_annotation,
)


def prepare_one_dataset(
    ds_dir: Union[str, Path],
    sample_length: int = 200,
    sample_freq: int = 10,
    download: bool = False,
    save_dataset: bool = False,
    output_path: Optional[Union[str, Path]] = None,
) -> pd.DataFrame:
    ds_dir.mkdir(parents=True, exist_ok=True)
    ds_dir = str(ds_dir) + "/"
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

    if save_dataset:
        pandas_samples.to_csv(output_path, index=False)

    return pandas_samples


if __name__ == "__main__":
    ecg_id_ds_dir = Path("../data/")
    datasets_dir = Path("../datasets/")
    datasets_dir.mkdir(parents=True, exist_ok=True)
    sample_frequencies = np.arange(6, 17, 2)
    sample_length = 200

    for sample_freq in sample_frequencies:
        download_ds = not ecg_id_ds_dir.exists()
        df = prepare_one_dataset(
            ecg_id_ds_dir,
            sample_length,
            sample_freq,
            download_ds,
            save_dataset=True,
            output_path=datasets_dir / f"full_{sample_freq}.csv",
        )
