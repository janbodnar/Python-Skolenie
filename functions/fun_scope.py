#!/usr/bin/python

# fun_scope.py

# a local variable is valid in the 
# function scope

name = "Jack"

def f():
   name = "Robert"
   print("Within function", name)

print("Outside function", name)
f()
