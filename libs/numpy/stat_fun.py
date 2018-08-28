#!/usr/bin/env python3

import numpy as np

a = np.array([[30,65,70], [80,95,20], [40,90,60]]) 

print(a)

print("median:")

print(np.median(a))
print(np.median(a, axis = 0))
print(np.median(a, axis = 1))

print("mean:")
print(np.mean(a))
print(np.mean(a, axis = 0))
print(np.mean(a, axis = 1))

print("average:")
print(np.mean(a))
print(np.mean(a, axis = 0))
print(np.mean(a, axis = 1))

print("Standard deviance")
print(np.std([1,2,3,4]))

print("Variance")
print(np.var([1,2,3,4]))
