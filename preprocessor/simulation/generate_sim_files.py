import os
import sys
import argparse

import pandas as pd


def parse_arguments(argv: list[str]) -> argparse.Namespace:
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    arg_parser.add_argument(
        "--dataset",
        type=str,
        action="store",
        required=True,
        help="Path to dataset csv file.",
    )

    arg_parser.add_argument(
        "--output-path",
        type=str,
        action="store",
        required=True,
        help="Output directiry path.",
    )

    return arg_parser.parse_args(argv)


def _generate_sim_file(values: list, idx: int) -> str:
    """Generates simulation testbench file

    Args:
        values (list): discrete heart rate
        idx (int): file idx

    Return:
        str: preprocessor testbench
    """
    file = [
        """*** preprocessor_tb.cir
.CONNECT GROUND 0
.GLOBAL GROUND

.INCLUDE preprocessor.sp
.INCLUDE components/DIODE.sp

.param xval=0

.LIB KEY=LIB_0 /mentor/tsmc/tsmclp65nm/models/eldo/crn65lp_v1d3.eldo TT

** Voltage Source
VPOWERVDD VDD GROUND 0.3v
V2 VSS GROUND 0.15v
    """
    ]

    file += [
        "** Preprocessor",
        f"xPREPROCESSOR {' '.join([f'IN{i}p IN{i}n' for i in range(len(values))])} OUT1 OUT2 GROUND VDD PREPROCESSOR",
    ]

    file += [
        """
** Output Diodes
xDIODE1 DOUT1 GROUND VDD DIODE
xDIODE2 DOUT2 GROUND VDD DIODE
    """
    ]

    file += [
        "** Input Source",
        "\n".join(
            [
                f"ICP_a{i} IN0p VSS DC {-values[i//2]}n"
                if i % 2 == 0
                else f"ICP_a{i} IN0n VSS DC {values[i//2]}n"
                for i in range(2 * len(values))
            ]
        ),
    ]

    file += [
        f"""
** Output Source
Voutp OUT1 DOUT1 0
Voutm OUT2 DOUT2 0 

** Simulation Params
.OPTIONS post
.dc param xval -0.01u 0.01u 0.01u

.printfile dc I(Voutp) file=preprocessor{idx}_p_samples.txt
.printfile dc I(Voutm) file=preprocessor{idx}_m_samples.txt

** Probes
.PROBE DC I(Voutp)
.PROBE DC I(Voutm)
.PROBE ALL

.end
    """
    ]
    return "\n".join(file)


def generate_sim_files(dataset: pd.DataFrame, output_dir: str) -> None:
    """Generates directory with testbenches

    Args:
        dataset (DataFrame): heart rate dataset
        output_dir (str): output path
    """
    if not os.path.isdir(output_dir):
        print(f"Creating dir {output_dir}")
        os.makedirs(output_dir, exist_ok=True)

    for idx, row in dataset.iterrows():
        values = list(row)[:-1]
        file = _generate_sim_file(values, idx)

        output_path = os.path.join(output_dir, f"preprocessor{idx}_tb.cir")

        with open(output_path, "w") as f:
            f.write(file)

    return


def main() -> None:
    args = parse_arguments(sys.argv[1:])

    dataset_path = args.dataset
    output_dir = args.output_path

    dataset = pd.read_csv(dataset_path)
    generate_sim_files(dataset, output_dir)

    return


if __name__ == "__main__":
    main()
