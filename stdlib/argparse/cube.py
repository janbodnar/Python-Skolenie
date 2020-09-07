#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('-v', type=int, required=True, help="computes cube")
parser.add_argument('--verbose', action='store_true', help="gives verbose output")
args = parser.parse_args()

val = args.v
cubed = val * val * val

if args.verbose:
    print(f'{val} cubed is {cubed}')
else:
    print(cubed)

