#!/usr/bin/python

import shutil

try:
    shutil.copy('myfile.txt', 'data/myfile.txt')
except IOError as e:
    print(e)
