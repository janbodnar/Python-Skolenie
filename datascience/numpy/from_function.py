#!/usr/bin/python

import numpy as np

# Construct an array by executing a function over each coordinate.

def f(x, y):
    return 2*x + y + 1

a = np.fromfunction(f, (5, 4), dtype=int)
print(a)

# anonymous functoin
b = np.fromfunction(lambda x, y: 2*x + y, (2, 2))
print(b)
