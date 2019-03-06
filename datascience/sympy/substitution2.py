#!/usr/bin/env python

from sympy import pprint, Symbol, sin, cos

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

expr = x**3 + 4*x*y - z
val = expr.subs([(x, 2), (y, 4), (z, 0)])
print(val)
