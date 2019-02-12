#!/usr/bin/python3

import os
from functools import partial
import sys

filetype = sys.argv[1]
data = os.listdir(os.curdir)
# print(data)

def isFileType(filetype, filename):

    # print(filetype)
    # print(filename)

    return os.path.isfile(filename) and filename.endswith('.{}'.format(filetype))

files = filter(partial(isFileType, filetype), os.listdir(os.curdir))

for myfile in files:
    print(myfile)



# directories = filter(os.path.isdir, os.listdir(os.curdir))

# for mydir in directories:
#     print(mydir)
