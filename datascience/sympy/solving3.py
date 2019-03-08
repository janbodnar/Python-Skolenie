#!/usr/bin/env python

from sympy.solvers import solveset
from sympy import Symbol, Interval, pprint

x = Symbol('x')

sol = solveset(x**2 - 1, x, Interval(0, 100))
print(sol) 
