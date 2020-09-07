#!/usr/bin/python

import numpy as np


a = np.array(
[ [1, -2, 3],
  [4, 5, 6],
  [-1, 0, -3]
])

print(a > 0)
print(a[a > 0])

f = (a < 0)
print(a[f])
