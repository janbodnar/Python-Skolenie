#!/usr/bin/python

# removing.py

items = { "coins": 7, "pens": 3, "cups": 2, 
    "bags": 1, "bottles": 4, "books": 5 }

print (items)

item = items.pop("coins")
print ("Item having value {0} was removed".format(item))

print (items)

del items["bottles"]
print (items)

items.clear()
print (items)
