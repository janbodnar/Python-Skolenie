#!/usr/bin/python3

# filter_fun.py

def positive(x):
    return x > 0

n = [-2, 0, 1, 2, -3, 4, 4, -1]

filtered = list(filter(positive, n))
print (filtered)
