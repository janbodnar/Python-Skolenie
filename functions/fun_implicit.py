#!/usr/bin/python

# fun_implicit.py

def power(x, y=2):

    r = 1
    
    for i in range(y):
       r = r * x
       
    return r

print (power(3))
print (power(3, 3))
print (power(5, 5))
