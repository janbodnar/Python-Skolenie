#!/usr/bin/python

# passing_by_reference.py

n = [1, 2, 3, 4, 5]

print ("Original list:", n)

def f(x):

    x.pop()
    x.pop()
    x.insert(0, 0)
    print ("Inside f():", x)    
    
f(n)    

print ("After function call:", n)
