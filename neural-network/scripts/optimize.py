import os
from itertools import product
from pickle import dump
from shutil import rmtree

import numpy as np
import pandas as pd
import tensorflow as tf
from activation_function import custom_sigmoid
from prepare_dataset_pipeline import get_datasets
from sklearn.preprocessing import MinMaxScaler


def build_model(hidden_neurons: int, l2_rate: float) -> tf.keras.Model:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=(10,), name="input"))
    model.add(
        tf.keras.layers.Dense(
            units=hidden_neurons,
            activation=custom_sigmoid,
            kernel_initializer="glorot_normal",
            kernel_regularizer=tf.keras.regularizers.L2(l2=l2_rate),
            use_bias=False,
        )
    )
    model.add(
        tf.keras.layers.Dense(
            units=1,
            activation="sigmoid",
            kernel_initializer="glorot_normal",
            kernel_regularizer=tf.keras.regularizers.L2(l2=l2_rate),
            use_bias=False,
        )
    )

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.Recall(name="recall"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.AUC(name="auc"),
        ],
    )

    return model


def fit_model(
    hidden_neurons: int,
    l2_rate: float,
    log_dir: str,
    train_set: tf.data.Dataset,
    val_set: tf.data.Dataset,
    test_set: tf.data.Dataset,
):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    model_log_dir = f"{log_dir}/model_{hidden_neurons}_{l2_rate}/"
    os.mkdir(model_log_dir)

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            patience=10, min_delta=1e-3, restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(patience=5, factor=0.2),
        tf.keras.callbacks.TensorBoard(log_dir=model_log_dir, histogram_freq=1),
    ]

    model = build_model(hidden_neurons, l2_rate)

    history = model.fit(
        x=train_set,
        validation_data=val_set,
        epochs=250,
        verbose=0,
        callbacks=callbacks,
    )

    print(f"{'#'*10} Val evaluation {'#'*10}")
    val_eval = model.evaluate(val_set, return_dict=True)
    print(f"{'#'*10} Test evaluation {'#'*10}")
    test_eval = model.evaluate(test_set, return_dict=True)

    model.layers[-1].activation = custom_sigmoid
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(threshold=0.0, name="accuracy"),
            tf.keras.metrics.Recall(name="recall"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.AUC(name="auc"),
        ],
    )

    print(f"{'#'*10} Test after change evaluation {'#'*10}")
    test_eval_after_change = model.evaluate(test_set, return_dict=True)

    return (model, history, val_eval, test_eval, test_eval_after_change)


if __name__ == "__main__":
    df = pd.read_csv("dataset.csv")
    train_set, val_set, test_set = get_datasets(
        df, scaler=MinMaxScaler(feature_range=(-1, 1))
    )

    log_dir = "./tensorboard_log"
    if os.path.exists(log_dir):
        rmtree(log_dir)

    hidden_neurons = list(range(8, 14, 2))
    l2_rates = [x / 1000 for x in range(5, 11)]

    for (hidden_neuron, l2_rate) in product(hidden_neurons, l2_rates):
        print(f"Trying: {hidden_neuron=}, {l2_rate=}")
        model, history, val_eval, test_eval, test_eval_after_change = fit_model(
            hidden_neurons=hidden_neuron,
            l2_rate=l2_rate,
            log_dir=log_dir,
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
            "params": {"hidden_neurons": hidden_neuron, "l2_rate": l2_rate},
            "history": history,
            "weights": model.get_weights(),
            "weights_ranges": weights,
            "val_eval": val_eval,
            "test_eval": test_eval,
            "test_eval_after_change": test_eval_after_change,
        }

        pickle_path = f"./models/neurons_{hidden_neuron}_l2_{l2_rate}.pkl"
        print(f"Weight ranges: {weights}")

        if np.all(np.abs(weights) < 1.5):
            with open(pickle_path, "wb") as f:
                dump(params, f)
