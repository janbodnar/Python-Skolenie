#!/usr/bin/python

"""
This is dirfun module
"""

import math, sys

version = 1.0

names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]

def show_names():

   for i in names:
      print (i)

print (dir(sys.modules['__main__']))
print (dir())

