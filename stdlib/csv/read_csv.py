#!/usr/bin/python3

# read_csv.py

import csv

f = open('numbers.csv', 'r')

with f:

    reader = csv.reader(f)
    
    for row in reader:
        print(row)
