#!/usr/bin/python

from sympy import pprint, Symbol, simplify

x = Symbol('x')

a = (x + 1)**2 - x*x
pprint(a)

b = simplify(a)
pprint(b)
