#!/usr/bin/env python

from sympy import expand, pprint
from sympy.abc import x

expr = (x + 1) ** 2

pprint(expr)

print('-----------------------')
print('-----------------------')

expr = expand(expr)
pprint(expr)
