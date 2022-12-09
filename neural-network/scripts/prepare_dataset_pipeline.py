from typing import Tuple

import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split


def get_datasets(
    dataset: pd.DataFrame,
    validation_size: float = 0.2,
    test_size: float = 0.1,
    batch_size: int = 32,
) -> Tuple[tf.data.Dataset]:
    """Converts a whole dataset into train, validation and test sets
       as tf.data.Dataset pipelines

    Args:
        dataset (pd.DataFrame): a dataframe containing X and y data

        validation_size (float, optional): the size of the validation
        set (in percent). Defaults to 0.2.

        test_size (float, optional): the size of the test set
        (in percent). Defaults to 0.1.

        batch_size (int, optional): the size of the batch during
        training. Defaults to 32.

    Returns:
        Tuple[tf.data.Dataset]: a tuple containing train, validation
        and test set pipelines
    """
    X, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train,
        y_train,
        test_size=1 - validation_size / (1 - test_size),
        stratify=y_train,
    )

    train_set = (
        tf.data.Dataset.from_tensor_slices((X_train, y_train))
        .batch(batch_size)
        .prefetch(3)
    )

    val_set = (
        tf.data.Dataset.from_tensor_slices((X_val, y_val))
        .batch(batch_size)
        .prefetch(3)
    )

    test_set = (
        tf.data.Dataset.from_tensor_slices((X_test, y_test))
        .batch(batch_size)
        .prefetch(3)
    )

    return (train_set, val_set, test_set)
