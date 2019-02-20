#!/usr/bin/env python3

import numpy as np

nums = [1, 4, 4, 6, 8, 10]

a = np.asarray(nums)

print(np.mean(a))
print(np.median(a))
print(np.average(a, weights=[4, 5, 5, 2, 1, 10]))
