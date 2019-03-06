#!/usr/bin/env python

import numpy
from sympy import Symbol, lambdify, sin, pprint

a = numpy.arange(10)

x = Symbol('x')

expr = sin(x)
f = lambdify(x, expr, "numpy")
pprint(f(a))
