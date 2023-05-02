import argparse
import os
import sys
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)


def parse_arguments(argv: List[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    arg_parser.add_argument(
        "--dataset",
        type=str,
        action="store",
        required=True,
        help="Directory with the test dataset",
    )

    arg_parser.add_argument(
        "--pred-dir",
        type=str,
        action="store",
        required=True,
        help="Directory with predictions from multiple models",
    )

    return arg_parser.parse_args(argv)


def read_true_values(dataset_path: str, frequency: int) -> np.array:
    df = pd.read_csv(f"{dataset_path}/test_{frequency}.csv")
    return df.iloc[:, -1].values.reshape(-1, 1)


def read_instance(pred_path: str, instance: int) -> int:
    m_data = np.loadtxt(
        f"{pred_path}/preprocessor{instance}_m_samples.txt",
        delimiter=" ",
        dtype="float",
    )
    p_data = np.loadtxt(
        f"{pred_path}/preprocessor{instance}_p_samples.txt",
        delimiter=" ",
        dtype="float",
    )

    return (
        1 if np.mean(p_data, axis=0)[1] - np.mean(m_data, axis=0)[1] > 0 else 0
    )


def read_predictions_for_model(pred_path: str) -> np.array:
    pred_files = os.listdir(pred_path)
    instances = set(
        [int(pred_name.split("_")[0][12:]) for pred_name in pred_files]
    )  # get all instance numbers
    preds = [
        (instance, read_instance(pred_path, instance)) for instance in instances
    ]
    preds_df = pd.DataFrame(data=preds, columns=["instance", "pred"])
    return preds_df.sort_values("instance")["pred"]


def calculate_metrics(y_true: np.array, y_pred: np.array) -> Dict[str, float]:
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
    }


def evaluate_model(model_pred_path: str, y_true: np.array) -> None:
    y_pred = read_predictions_for_model(model_pred_path)
    metrics = calculate_metrics(y_true, y_pred)
    model_description = model_pred_path.split("/")[-1]
    n_neurons = model_description.split("n")[0]
    l2_rate = model_description.split("-")[-1]
    print(f"\tModel: {n_neurons=}, {l2_rate=}, {metrics=}")


if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    dataset_path = args.dataset
    samples_dir = args.pred_dir
    all_frequency_paths = os.listdir(samples_dir)
    all_frequency_values = [
        int(freq.split("_")[-1]) for freq in all_frequency_paths
    ]
    all_frequency_y_true = {
        freq_val: read_true_values(dataset_path, freq_val)
        for freq_val in all_frequency_values
    }

    for freq in all_frequency_values:
        print(f"Frequency: {freq}")
        all_models_path = os.listdir(f"{samples_dir}/sample_freq_{freq}")
        for model_path in all_models_path:
            y_true = read_true_values(dataset_path, freq)
            try:
                evaluate_model(
                    f"{samples_dir}/sample_freq_{freq}/{model_path}", y_true
                )
            except Exception:
                pass
