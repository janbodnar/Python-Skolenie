#!/usr/bin/python

# attributes_dynamic.py

class Person:
   pass

p = Person()
p.age = 24
p.name = "Peter"

print("{0} is {1} years old".format(p.name, p.age))
