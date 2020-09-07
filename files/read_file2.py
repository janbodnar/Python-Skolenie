#!/usr/bin/python

# read_file2.py

import sys

with open('works.txt', 'r') as f:

    while True:
        
        line = f.readline()
        
        if not line: 
            break
        else: 
            print(line.rstrip())
