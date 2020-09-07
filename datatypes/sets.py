#!/usr/bin/python

set1 = set(['a', 'b', 'c', 'c', 'd'])
set2 = set(['a', 'b', 'x', 'y', 'z'])

print ("set1: " , set1)
print ("set2: " , set2)
print ("intersection: ", set1 & set2)
print ("union: ", set1 | set2)
print ("difference: ", set1 - set2)
print ("symmetric difference: ", set1 ^ set2)
