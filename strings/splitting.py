#!/usr/bin/python

# splitting.py

nums = "1,5,6,8,2,3,1,9"

k = nums.split(",")
print (k)

l = nums.split(",", 5)
print (l)

m = nums.rsplit(",", 3)
print (m)
