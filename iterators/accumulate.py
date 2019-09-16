#!/usr/bin/env python

data = [1, 2, 3, 4, 5, 6, 7, 8]

result = itertools.accumulate(data, operator.mul)

for each in result:
    print(each)
