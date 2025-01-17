#!/usr/bin/python

import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('var is negative')
else:
    print('is zero')
