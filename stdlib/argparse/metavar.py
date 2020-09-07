#!/usr/bin/python

import argparse

# metavar gives name to the expected value 
# in error and help outputs

parser = argparse.ArgumentParser()
   
parser.add_argument('-v', type=int, required=True, metavar='value', 
    help="computes cube for the given value")
args = parser.parse_args()

print(args)

val = args.v

print(val * val * val)
