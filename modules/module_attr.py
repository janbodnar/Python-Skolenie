#!/usr/bin/python

# module_attr.py

from animals import Cat

class Being:
   pass


b = Being()
print (b.__module__)

c = Cat()
print (c.__module__)
