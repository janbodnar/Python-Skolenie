#!/usr/bin/python

import argparse
import sys

# nargs sets the required number of argument values
# metavar gives name to argument values in error and help output

parser = argparse.ArgumentParser()
parser.add_argument('chars', type=str, nargs=2, metavar='c',
                    help='starting and ending character')

args = parser.parse_args()

try:
    v1 = ord(args.chars[0])
    v2 = ord(args.chars[1])

except TypeError as e:

    print('Error: arguments must be characters')
    parser.print_help()
    sys.exit(1)

if v1 > v2:
    print('first letter must precede the second in alphabet')
    parser.print_help()
    sys.exit(1)

for o in range(v1, v2 + 1):
    print(chr(o), end=' ')

