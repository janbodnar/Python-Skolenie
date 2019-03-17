#!/usr/bin/env python

import argparse

# + nargs expects 1+ arguments

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='+')
args = parser.parse_args()

print(f"The sum of values is {sum(args.num)}")