#!/usr/bin/python

import os

files = filter(os.path.isfile, os.listdir(os.curdir))

for myfile in files:
    print(myfile)

# files = [myfile for myfile in os.listdir('.') if os.path.isfile(os.path.join('.', myfile))]
# print(files)

# for fname in os.listdir('.'):
#     if os.path.isdir(fname):
#        pass  
#     else:
#        pass  
