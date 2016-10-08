#!/usr/bin/python

# global_kwd.py

x = 15

def function():
   global x
   x = 45

function()
print x
