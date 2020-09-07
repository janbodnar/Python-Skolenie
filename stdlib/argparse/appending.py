#!/usr/bin/python

import argparse

# append action allows to group repeating
# options

parser = argparse.ArgumentParser()
   
parser.add_argument('-n', '--name', dest='names', action='append', 
    help="provides names to greet")

args = parser.parse_args()

names = args.names

for name in names:
    print(f'Hello {name}!')