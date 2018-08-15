#!/usr/bin/python3

# recapitulation
# recap.py

import random
import os

# ******************************      
# os module

print(os.version)

print("******************************") 

# ******************************      
# list, for loop, built-ins

nums = [1, 2, 3, 4, 5]

print("There are {0} elements in the list".format(len(nums)))

for e in nums:
    print(e, end=' ')
    
print()    

print("maximum: {0}".format(max(nums)))
print("maximum: {0}".format(max(nums)))
print("summation: {0}".format(sum(nums)))


# ******************************      

male = False
male = bool(random.randint(0, 1))

if (male):
   print("We will use name John")
else:
   print("We will use name Victoria")
   
 
print("******************************") 

# ******************************      
# dictionary   

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(capitals)


for k, v in weekend.items():
    print("key: {0}, value: {1}".format(k, v))

print("******************************")

# ******************************      
# while loop

i = len(nums) - 1
mysum = 0

while (i >= 0):
    
    mysum += nums[i]
    i -= 1
    

print("summation 2: {0}".format(mysum))

print("******************************")

# ******************************      
# sets

set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1.intersection(set2))
print("union:", set1.union(set2))
print("difference:", set1.difference(set2))
print("symmetric difference:", set1.symmetric_difference(set2))
