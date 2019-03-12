#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

dirs = [e for e in path.iterdir() if e.is_dir()]
print(dirs)