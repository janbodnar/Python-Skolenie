#!/usr/bin/env python3

import numpy as np

a = np.arange(9)
print(a)

a2 = a.reshape((3, 3))
print(a2)

print(np.sum(a2))
