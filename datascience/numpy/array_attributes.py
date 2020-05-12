#!/usr/bin/env python3

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

# the number of axes (dimensions) of the array
print(f'# of array dimensions: {a.ndim}')

# the dimensions of the array - a tuple of
# integers indicating the size of the array in each dimension.
print(f'array shape: {a.shape}')

# total number of elements in the array
print(f'# of elements: {a.size}')

# an object describing the type of the elements in the array
print(f'type of elements: {a.dtype}')

# the size in bytes of each element of the array
print(f'element size in bytes {a.itemsize}')
