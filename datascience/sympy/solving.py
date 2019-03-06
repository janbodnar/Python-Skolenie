#!/usr/bin/env python

'''
Solving expressions
'''

from sympy import pprint, Symbol, solve

x = Symbol('x')

sol = solve(x**2 - x, x)

pprint(sol)
