#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

files = [e for e in path.iterdir() if e.is_file()]
print(files)