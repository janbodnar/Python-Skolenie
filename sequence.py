#!/usr/bin/env python

import numpy

# create sequence of values from 100 to 1000

# 1
vals = numpy.linspace(100, 1000, 900, dtype=int)
 print(vals)

# 2
vals2 = []

for i in range(100, 1001):
    vals2.append(i)

print(vals2)

# 3

i = 0
start = 100
step = 1
end = 1000
vals3 = []

while i + start <= end:

    vals3.append(start + i)
    i += 1

print(vals3)

# 4

def seq():

    start = 100
    end = 1000

    while start <= end:

        yield start
        start += 1

vals4 = []

for e in seq():

    vals4.append(e)

print(vals4)
