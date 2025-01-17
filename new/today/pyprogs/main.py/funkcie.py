#!/usr/bin/python

# fahrenheit.py

def cel_to_fahr(c):
    return c * 9/5 + 32

f1 = cel_to_fahr(100)
f2 = cel_to_fahr(0)
f3 = cel_to_fahr(30)

print(f1)
print(f2)
print(f3)

##################################

def twice(x):
    return x * 2

print(twice(2)) 


##################################
def cube(x):
    return pow(x, 3) # x * x * x

print(cube(2)) 

##################################
from math import sqrt

print(sqrt(4))