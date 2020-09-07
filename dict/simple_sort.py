#!/usr/bin/python

# simple_sort.py

items = { "coins": 7, "pens": 3, "cups": 2, 
    "bags": 1, "bottles": 4, "books": 5 }
    
kitems = list(items.keys())
kitems.sort()

for k in kitems:
    print (": ".join((k, str(items[k]))))
