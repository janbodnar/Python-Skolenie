#!/usr/bin/env python

import argparse
from pathlib import Path

# working with positional arguments

parser = argparse.ArgumentParser()
   
parser.add_argument('f', type=str, help='file name')
parser.add_argument('n', type=int, help='show n lines from the top')

args = parser.parse_args()

filename = args.f

lines = Path(filename).read_text().splitlines()

for line in lines[:args.n]:
    print(line) 

