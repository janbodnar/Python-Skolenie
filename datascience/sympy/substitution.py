#!/usr/bin/env python

from sympy import pprint, Symbol, sin, cos

x = Symbol('x')
y = Symbol('y')

expr = cos(x) + sin(x)

val = expr.subs(x, 0)
print(val)

val = expr.subs(x, 1)
print(val)
print(val.evalf(10))
