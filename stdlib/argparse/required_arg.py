#!/usr/bin/python

import argparse

# positional args

parser = argparse.ArgumentParser()
   
parser.add_argument('--name', required=True)

args = parser.parse_args()

print(f'Hello {args.name}')
