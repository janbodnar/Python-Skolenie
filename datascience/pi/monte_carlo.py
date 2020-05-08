#!/usr/bin/python

from random import random
from math import sqrt

n = 100_000
count = 0

for i in range(n):
    # check random.uniform
    x, y = random(), random()

    r = sqrt(pow(x, 2) + pow(y, 2))

    if r < 1:
        count +=1

print(4 * count / n)
