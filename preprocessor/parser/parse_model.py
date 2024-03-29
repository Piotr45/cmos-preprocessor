import sys
import pickle
import argparse
import numpy as np

import keras.backend as K
from keras.utils import get_custom_objects

from model_parser import ModelParser


def custom_sigmoid(x):
    return 2 * K.sigmoid(37 * x) - 1

get_custom_objects()["custom_sigmoid"] = custom_sigmoid

def parse_arguments(argv: list[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    arg_parser.add_argument(
        "--model",
        type=str,
        action="store",
        required=True,
        help="Path to file, that contains TensorFlow model",
    )

    arg_parser.add_argument(
        "--grid",
        type=str,
        action="store",
        required=True,
        help="Path to file, that contains weight grid",
    )

    return arg_parser.parse_args(argv)


def load_model(path: str) -> np.array:
    with open(path, "rb") as file:
        data = pickle.load(file)
        return data["weights"]


def load_grid(path: str) -> list:
    with open(path, "r") as file:
        grid = {}
        for line in file.read().split("\n")[:-1]:
            code, weight = line.split("\t")
            grid[code] = float(weight)
        return {key: val for key, val in sorted(grid.items(), key=lambda v: v[1])}


def main() -> None:
    args = parse_arguments(sys.argv[1:])

    nn = load_model(args.model)
    grid = load_grid(args.grid)

    modelParser = ModelParser(nn, grid)
    result = modelParser.parse_model()

    with open("../preprocessor.sp", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
