#!/usr/bin/python

from sympy import sin, limit, oo
from sympy.abc import x

l1 = limit(1/x, x, oo)
print(l1)

l2 = limit(1/x, x, 0)
print(l2)
