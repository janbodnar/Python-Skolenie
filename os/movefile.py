#!/usr/bin/python3

import shutil

try:
    shutil.move('myfile.txt', 'data/myfile.txt')
except IOError as e:
    print(e)
