#!/usr/bin/python

import itertools

shapes = ['circle', 'triangle', 'square']

result = itertools.combinations(shapes, 2)

for each in result:
    print(each)
