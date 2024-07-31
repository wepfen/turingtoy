#!/usr/bin/env python3
from src.turingtoy import run_turing_machine
from pathlib import Path

import argparse




def main(*args):

	parser = argparse.ArgumentParser(description='Run the turing machine')
	parser.add_argument('--json', type=str, nargs=1, required=True, dest="json",
						help='Run the machine with the instruction specified in the json file')

	args = parser.parse_args()
	instruction_file = args.json
	print(json_file)

	if not Path(instruction_file).exists():
		print("test")




if __name__ == "__main__":
	main()
