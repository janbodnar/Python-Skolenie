#!/usr/bin/python

# list_comprehension3.py

a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [ e**2 for e in a_list if type(e) == int ]

print (squared_ints)
