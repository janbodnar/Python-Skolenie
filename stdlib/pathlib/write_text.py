#!/usr/bin/python3

from pathlib import Path

path = Path('myfile.txt')
path.touch()

path.write_text('This is myfile.txt')