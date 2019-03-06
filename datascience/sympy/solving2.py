#!/usr/bin/env python

'''
Solving expressions
'''

from sympy import pprint, symbols, solveset

x, y, z = symbols('x y z')

sol = solveset(x + y + z - 3, x)

pprint(sol)
print(sol)
