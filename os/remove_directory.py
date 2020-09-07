#!/usr/bin/python

import os

def removeDirectory(directory):
    try:
        if os.path.exists(directory):
            os.rmdir(directory)
    except OSError:
        print('failed to remove directory ' +  directory)

removeDirectory('mydata')
