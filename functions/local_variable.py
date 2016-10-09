#!/usr/bin/python3

# local_variable.py

name = "Jack"

def f():
   name = "Robert"
   print ("Within function", name)

print ("Outside function", name)
f()
