#!/usr/bin/env python

import argparse
import datetime
import time

# choices limits argument values to the 
# given list

parser = argparse.ArgumentParser()

parser.add_argument('--now', dest='format', choices=['std', 'iso', 'unix', 'tz'],
                    help="shows datetime in given format")

args = parser.parse_args()
fmt = args.format

if fmt == 'std':
    print(datetime.date.today())
elif fmt == 'iso':
    print(datetime.datetime.now().isoformat())
elif fmt == 'unix':
    print(time.time())
elif fmt == 'tz':
    print(datetime.datetime.now(datetime.timezone.utc))
