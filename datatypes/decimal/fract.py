#!/usr/bin/python

from decimal import Decimal
from fractions import Fraction

x = Decimal(1) / Decimal(3)
y = x * Decimal(3)

print(y == Decimal(1))
print(x)
print(y)

print("-----------------------")

u = Fraction(1) / Fraction(3)
v = u * Fraction(3)

print(v == 1)
print(u)
print(v)
