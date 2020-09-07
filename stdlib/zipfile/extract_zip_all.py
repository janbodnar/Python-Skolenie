#!/usr/bin/python

import zipfile

with zipfile.ZipFile('myfile.zip') as zf:
    
    zf.extractall('extracted')
