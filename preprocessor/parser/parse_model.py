import pickle
import numpy as np

from model_parser import ModelParser


def load_model(path: str) -> np.array:
    with open(path, "rb") as file:
        return pickle.load(file)


def load_grid(path: str) -> list:
    with open(path, 'r') as file:
        grid = {}
        for line in file.read().split("\n")[:-1]:
            code, weight = line.split("\t")
            grid[code] = float(weight)
        return {key: val for key, val in sorted(grid.items(), key=lambda v:v[1])}


def main() -> None:
    nn = load_model("../../resources/weights_small.pkl")
    grid = load_grid("../../resources/grid.txt")

    modelParser = ModelParser(nn, grid)
    result = modelParser.parse_model()

    with open("../preprocessor.sp", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
