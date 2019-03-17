#!/usr/bin/env python

import argparse

# required defines a mandatory argument 
# default defines a defautl value if not specified

parser = argparse.ArgumentParser()

parser.add_argument('-b', type=int, required=True, help="defines the base value")
parser.add_argument('-e', type=int, default=2, help="defines the exponent value")
args = parser.parse_args()

val = 1

base = args.b
exp = args.e

for i in range(exp):
    val *= base

print(val)

