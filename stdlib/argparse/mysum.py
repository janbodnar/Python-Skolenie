#!/usr/bin/env python

import argparse

# nargs sets the required number of argument 
# values

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs=3)
args = parser.parse_args()

print(f"The sum of values is {sum(args.num)}")