#!/usr/bin/python

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))

print("**********************")

# Elementwise difference
print(x - y)
print(np.subtract(x, y))

print("**********************")

# Elementwise product
print(x * y)
print(np.multiply(x, y))

print("**********************")

# Elementwise division
print(x / y)
print(np.divide(x, y))

print("**********************")

# Elementwise square root
print(np.sqrt(x))


