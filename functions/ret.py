#!/usr/bin/python

"""
The ret.py script shows how to work with
functions in Python. 
Author: Jan Bodnar
ZetCode, 2016
"""

def showModuleName():
    
    print (__doc__)

def getModuleFile():
    
   return (__file__)

a = showModuleName()
b = getModuleFile()

print (a, b)
