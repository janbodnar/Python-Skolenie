#!/usr/bin/python

from pathlib import Path

path = Path('words.txt')

with path.open() as f: 
    lines = f.readlines()
    print(lines)

for line in lines:
    print(line.rstrip())