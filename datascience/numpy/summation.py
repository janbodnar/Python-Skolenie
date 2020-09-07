#!/usr/bin/python

import numpy as np

x = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

print(x)

print(np.sum(x))  
print(np.sum(x, axis=0))  
print(np.sum(x, axis=1))  
