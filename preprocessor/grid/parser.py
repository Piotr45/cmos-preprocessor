import sys
import argparse
import string
import pathlib as pl


FREQ = 0.0005


def parse_arguments(argv: list[str]) -> argparse.Namespace:
  arg_parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  arg_parser.add_argument(
    "--input-p",
    type     = str,
    action   = "store",
    required = True,
    help     = ""
  )

  arg_parser.add_argument(
    "--input-m",
    type     = str,
    action   = "store",
    required = True,
    help     = ""
  )

  return arg_parser.parse_args(argv)


def read_file(path: str) -> list:
  with open(path, 'r') as file:
    readline = file.read().split("\n")
    return readline


def reformat_input(lines: list) -> list:
  for i, line in enumerate(lines):
    if i < 2:
      continue
    lines[i] = tuple(map(float, line.split(' ')[1:]))
  
  return lines[2:-1]


def inverse_binary(binary: str) -> str:
  result = ""
  for bit in binary:
    if bit == "1":
      result += "0"
    else:
      result += "1"
  return result


def decode_binaries(outm: list[tuple, ], outp: list[tuple, ], _in : int) -> list[tuple, ]:
  binaries = []
  for m, p in zip(outm, outp):
    binary = str.zfill("{0:b}".format(int(m[0] / FREQ)), 12)
    binary = inverse_binary(binary)
    value  = (p[1] - m[1]) / (2 * _in)

    binaries.append(f"{binary}\t{value}\n")
  return binaries


def main() -> None:
  args = parse_arguments(sys.argv[1:])
  
  input_m = pl.Path(args.input_m)
  input_p = pl.Path(args.input_p)
  
  lines_m = read_file(input_m)
  lines_p = read_file(input_p)
  
  preprocessed_m = reformat_input(lines_m)
  preprocessed_p = reformat_input(lines_p)

  output = decode_binaries(preprocessed_m, preprocessed_p, 10**(-9))
  
  output_path = input_m.parent / "grid.txt"

  with open(output_path, 'w') as file:
    for row in output:
      file.write(f"{row}")


if __name__ == "__main__":
  main()