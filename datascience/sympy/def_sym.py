#!/usr/bin/env python

# ways to define symbols

from sympy import Symbol, symbols
from sympy.abc import x, y

expr = 2*x + 5*y
print(expr)

a = Symbol('a')
b = Symbol('b')

expr2 = a*b + a - b
print(expr2)

i, j = symbols('i j')
expr3 = 2*i*j + i*j
print(expr3) 
