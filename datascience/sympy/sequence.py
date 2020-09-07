#!/usr/bin/python

from sympy import summation, sequence, pprint
from sympy.abc import x

s = sequence(x, (x, 1, 10))
print(s)
pprint(s)
print(list(s))

print(s.length)

print(summation(s.formula, (x, s.start, s.stop)))
# print(sum(list(s)))
