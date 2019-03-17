#!/usr/bin/env python

import argparse
import datetime

# dest gives a different name to a flag

parser = argparse.ArgumentParser()
   
parser.add_argument('-n', dest='now', action='store_true', help="shows now")

args = parser.parse_args()

# we can refer to the flag
# by a new name
if args.now:

    now = datetime.datetime.now()
    print(f"Now: {now}")
