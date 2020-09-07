#!/usr/bin/python

import numpy as np

a = np.array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])

print(a[:2,:2])
print(a[:3,:3])

print("*********************")

print(a[0,...])
print(a[...,:3])
