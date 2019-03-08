#!/usr/bin/env python

'''
Solving equation
'''

from sympy import pprint, Symbol, solve

x = Symbol('x')

sol = solve(x**2 - x, x)

pprint(sol)
