import sys
import argparse

from typing import Tuple


def parse_arguments(argv: list[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    arg_parser.add_argument(
        "--preprocessor",
        type=str,
        action="store",
        required=True,
        help="Path to preprocessor file.",
    )

    return arg_parser.parse_args(argv)


def _count_components(preprocessor_path: str) -> Tuple[int, Tuple[int, int, int, int]]:
    component_counter = [0, 0, 0, 0]
    current_mirror_size = 0

    with open(preprocessor_path, "r") as f:
        for line in f.readlines():
            splitted = line.split()

            # Skip empty lines
            if not splitted:
                continue

            first = splitted[0]

            if "CMRR" in first:
                component_counter[0] += 1
            elif "DENDRITE" in first:
                component_counter[1] += 1
            elif "AXON" in first:
                component_counter[2] += 1
            elif "CM" in first:
                component_counter[3] += 1
                current_mirror_size = int(splitted[-1].split("CM")[-1])

    return current_mirror_size, component_counter


def _calculate_cm_size(size: int) -> float:
    mn0 = 0.265 * 0.835
    mp0 = 2.075 * 0.835

    mnN = 0.58 * 0.5
    mpN = 2.05 * 0.5
    return mn0 + mp0 + size * (mnN + mpN)


def _calculate_cmrr_size() -> float:
    cm1 = 0.265 * 0.835 + 2.075 * 0.835 + 2 * 0.58 * 0.5 + 2 * 2.05 * 0.5
    cm2 = 0.465 * 0.115 + 2.075 * 0.115 + 2 * 0.605 * 0.5 + 2 * 2.53 * 0.5
    return 2 * cm1 + cm2


def _calculate_axon_size() -> float:
    mirror = 0.265 * 5.535 + 2.075 * 5.535 + 0.14 * 0.5 + 0.14 * 0.5
    inverter = 0.14 * 14.4 + 5.7 * 14.4 + 0.14 * 14.4 + 5.7 * 14.4
    inm = mirror
    return mirror + 2 * inverter + inm


def _calculate_dendrite_size() -> float:
    tg = 4 * 20 * 0.06 + 0.32 * 0.06 + 1.18 * 0.06

    dendrite_core = (
        6 * tg
        + 0.06 * (0.25 + 0.58 + 0.265 + 0.68)
        + 0.8 * (0.265 + 2.35)
        + 7.8 * (0.14 + 8.25)
        + 20 * (0.14 + 8.7)
        + 15 * 2 * (11.15 + 0.14)
        + 20 * 2 * (0.14 + 12.6)
    ) * 2

    cmrr = _calculate_cmrr_size()
    return 2 * dendrite_core + cmrr


def _calculate_transistors_num(
    cmrrs: int, dendrites: int, axons: int, cms: int, cms_size: int
) -> int:
    return (
        cmrrs * 18 + cms * (2 + 2 * cms_size) + axons * 16 + dendrites * 234
    )  # 2 * (18 * 2 + 12 * 6) + 18


def _calculate_active_area(
    cmrrs: int, dendrites: int, axons: int, cms: int, cms_size: int
) -> float:
    return (
        cmrrs * _calculate_cmrr_size()
        + dendrites * _calculate_dendrite_size()
        + axons * _calculate_axon_size()
        + cms * _calculate_cm_size(cms_size)
    )


def calculate_stats(preprocessor_path: str) -> None:
    current_mirror_size, (cmrrs, dendrites, axons, current_mirrors) = _count_components(
        preprocessor_path
    )

    transisors_num = _calculate_transistors_num(
        current_mirror_size, cmrrs, dendrites, axons, current_mirrors
    )
    active_area = _calculate_active_area(
        current_mirror_size, cmrrs, dendrites, axons, current_mirrors
    )

    print(
        f"STATISTICS\nNumber of components:\n CM{current_mirror_size}: {current_mirrors}\n CMRR: {cmrrs}\n DENDRITE: {dendrites}\n AXON: {axons}"
    )
    print(
        f"Number of transistors: {transisors_num}\nActive area [um^2]: {round(active_area, 4)}"
    )
    return


def main() -> None:
    args = parse_arguments(sys.argv[1:])

    preprocessor_path = args.preprocessor

    calculate_stats(preprocessor_path)
    return


if __name__ == "__main__":
    main()
