from model_parser import ModelParser
from mod.axon import Axon


def main() -> None:
    xAK1 = Axon("v_B", "out1s", "vss", "vdd", "AK_out")
    print(xAK1)


if __name__ == "__main__":
    main()
