import sys
import argparse
import string
import pathlib as pl


FREQ = 0.0005


def parse_arguments(argv: list[str]) -> argparse.Namespace:
  arg_parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  arg_parser.add_argument(
    "--input",
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


def decode_binaries(data: list[tuple, ]) -> list[tuple, ]:
  binaries = []
  for time, value in data:
    binary = str.zfill("{0:b}".format(int(time / FREQ)), 12)
    binaries.append((binary, value * 10**9))
  return binaries


def main() -> None:
  args = parse_arguments(sys.argv[1:])
  
  file_path = pl.Path(args.input)
  
  lines = read_file(file_path)
  data  = reformat_input(lines)
  
  # 0000 0000 0000 0001 == 0.0005 s
  # 0000 0000 0000 0010 == 0.001  s
  # 0000 0000 0000 0011 == 0.0015 s

  output = decode_binaries(data)
  
  output_path = file_path.parent / "out.txt"

  with open(output_path, 'w') as file:
    for row in output:
      file.write(f"{row}")


if __name__ == "__main__":
  main()