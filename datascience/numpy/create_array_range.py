#!/usr/bin/env python

import numpy as np

start, end, step = 0, 10, 2

# uses f-string debugging, requires Python 3.8

print(f'{np.arange(start, end) = }')
print(f'{np.arange(start, end, step) = }')

n = 20 # number of values to generate
print(f'{np.linspace(start, end, n) = }')
