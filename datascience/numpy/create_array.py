#!/usr/bin/env python3

import numpy as np

# from Python lists
a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1)

# array of zeros
a2 = np.zeros((2, 2))
print(a2)

# array of oness
a3 = np.ones((2, 2))    # Create an array of all ones
print(a3)              # Prints "[[ 1.  1.]]"

# array of predefined values
a4 = np.full((2, 2), 5)
print(a4)

# identity matrix
a5 = np.eye(3)
print(a5)

# array of random values
a6 = np.random.random((3, 3))
print(a6)
