#!/usr/bin/env python

from sympy import pprint, Symbol, Eq, solve

x = Symbol('x')

eq1 = Eq(x + 1, 4)
pprint(eq1)

sol = solve(eq1, x)
print(sol)
