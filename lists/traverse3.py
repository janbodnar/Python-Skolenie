#!/usr/bin/python

# traverse3.py

n = [1, 2, 3, 4, 5]

print (list(enumerate(n)))

for e, i in enumerate(n):
    print ("n[%d] = %d" % (e, i))
