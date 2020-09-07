#!/usr/bin/python

from pathlib import Path
from os import chdir

path = Path('..')

print(f'Current working directory: {path.cwd()}')

chdir(path)

print(f'Current working directory: {path.cwd()}')

chdir('..')