from itertools import product
from multiprocessing import Pool
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from pickle import dump
from sklearn.preprocessing import MinMaxScaler

from optimize import fit_model
from prepare_dataset_pipeline import get_datasets


def train_model(
    hidden_neuron: int,
    sample_freq: int,
    l2_rate: float,
    datasets_path: Path,
    models_path: Path,
):
    warnings.filterwarnings("ignore")
    full_dataset_path = datasets_path / f"full_{sample_freq}.csv"
    df = pd.read_csv(full_dataset_path)

    test_set_path = datasets_path / f"test_{sample_freq}.csv"
    save_test_set = not test_set_path.exists()

    train_set, val_set, test_set = get_datasets(
        df,
        scaler=None,
        save_test_set=save_test_set,
        saving_path=test_set_path,
    )

    model, history, val_eval, test_eval, test_eval_after_change = fit_model(
        input_length=sample_freq,
        hidden_neurons=hidden_neuron,
        l2_rate=l2_rate,
        train_set=train_set,
        val_set=val_set,
        test_set=test_set,
    )

    weights = (
        np.min(model.get_weights()[0]),
        np.max(model.get_weights()[0]),
        np.min(model.get_weights()[1]),
        np.max(model.get_weights()[1]),
    )

    params = {
        "params": {
            "hidden_neurons": hidden_neuron,
            "sample_freq": sample_freq,
            "l2_rate": l2_rate,
        },
        "history": history,
        "weights": model.get_weights(),
        "weights_ranges": weights,
        "val_eval": val_eval,
        "test_eval": test_eval,
        "test_eval_after_change": test_eval_after_change,
    }

    pickle_path = (
        models_path
        / f"sample_freq_{sample_freq}_neurons_{hidden_neuron}_l2_{l2_rate}.pkl"
    )
    print(f"Weight ranges: {weights}")

    if np.all(np.abs(weights) < 1.5):
        with open(pickle_path, "wb") as f:
            dump(params, f)


if __name__ == "__main__":
    datasets_path = Path("../datasets/")
    models_path = Path("../models/")
    models_path.mkdir(parents=True, exist_ok=True)
    hidden_neurons = np.arange(6, 17, 2)
    sample_frequencies = np.arange(6, 17, 2)
    l2_rates = np.arange(0.05, 0.11, 0.01)

    parameters = product(hidden_neurons, sample_frequencies, l2_rates)
    pool_parameters = [(*p, datasets_path, models_path) for p in parameters]
    with Pool(6) as p:
        p.starmap(train_model, pool_parameters)
