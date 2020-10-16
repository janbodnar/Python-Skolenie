#!/usr/bin/python

from sympy import Rational

r1 = Rational(1/10)
r2 = Rational(1/10)
r3 = Rational(1/10)

val = (r1 + r2 + r3) * 3
print(val.evalf())

val2 = (1/10 + 1/10 + 1/10) * 3
print(val2)
