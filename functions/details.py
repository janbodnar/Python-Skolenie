#!/usr/bin/python3

# details.py

def display(**details):

   for i in details:
      print ("%s: %s" % (i, details[i]))


display(name="Lary", age=43, sex="M")
