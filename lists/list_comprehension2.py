#!/usr/bin/python3

# list_comprehension2.py

lang = "Python"

a = []
for e in lang:
    a.append(ord(e))

b = [ord(e) for e in lang]

print (a)
print (b)
