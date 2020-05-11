#!/usr/bin/python

from random import random
from math import sqrt
from timeit import default_timer as timer


def pi(n):

    count = 0

    for i in range(n):

        x, y = random(), random()

        r = sqrt(pow(x, 2) + pow(y, 2))

        if r < 1:
            count += 1

    return 4 * count / n


start = timer()
pi_est = pi(100_000_000)
end = timer()

print(f'elapsed time: {end - start}')
print(f'π estimate: {pi_est}')
