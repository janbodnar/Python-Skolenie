#!/usr/bin/env python

from sympy import pprint, Symbol, sin, cos

x = Symbol('x')

a = cos(x)**2 - sin(x)**2
b = cos(2*x)

print(a.equals(b))

# we cannot use == operator
print(a == b)
