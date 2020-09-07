#!/usr/bin/python

# deep_copy.py

import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = copy.copy(c)

print(id(d[0]) == id(c[0]))

a[0] = 11
print (d[0][0])


print ("**********************")


e = copy.deepcopy(c)

print(id(e[0]) == id(c[0]))

a[1] = 22
print (e[0][1])
print (e[0])
