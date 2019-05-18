#!/usr/bin/env python3

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

# the number of axes (dimensions) of the array
print('# of array dimensions: {}'.format(a.ndim))

# the dimensions of the array - a tuple of 
# integers indicating the size of the array in each dimension.
print('array shape: {}'.format(a.shape))

# total number of elements in the array
print('# of elements: {}'.format(a.size))

# an object describing the type of the elements in the array
print('type of elements: {}'.format(a.dtype))

# the size in bytes of each element of the array
print('element size in bytes {}'.format(a.itemsize))
