#!/usr/bin/python

from pathlib import Path

path = Path('myfile.txt')
path.touch()

path.write_text('This is myfile.txt')