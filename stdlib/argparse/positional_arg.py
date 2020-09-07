#!/usr/bin/python

import argparse

# positional args

parser = argparse.ArgumentParser()
   
parser.add_argument('name')
parser.add_argument('age')

args = parser.parse_args()

print(f'{args.name} is {args.age} years old')
