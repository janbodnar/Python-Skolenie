#!/usr/bin/python

import zipfile

with zipfile.ZipFile('subor.zip', 'r') as zf:
    print(zf.namelist())
