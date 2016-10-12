#!/usr/bin/python3

# scan_dir.py

import os

for file in os.scandir('.'):

    line = ''

    if file.is_file():
        line += 'f'
    elif file.is_dir():
        line += 'd'
    elif file.is_symlink():
        line += 'l'

    line += '\t'

    print("{}{}".format(line, file.name))
