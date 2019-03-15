#!/usr/bin/env python

import collections
from pathlib import Path

docs = Path.home() / 'Documents'

files = [path.suffix for path in docs.iterdir() if path.is_file() and path.suffix]
data = collections.Counter(files)

print(data)

for key, val in data.items(): 
    print(f'{key}: {val}')