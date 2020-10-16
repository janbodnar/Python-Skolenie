#!/usr/bin/python

from decimal import Decimal, getcontext
import math

import mpmath

getcontext().prec = 50
mpmath.mp.dps = 50
num = Decimal(1) / Decimal(7)

num2 = mpmath.mpf(1) / mpmath.mpf(7)

print("   math.sqrt: {0}".format(Decimal(math.sqrt(num))))
print("decimal.sqrt: {0}".format(num.sqrt()))
print(" mpmath.sqrt: {0}".format(mpmath.sqrt(num2)))
print('actual value: 0.3779644730092272272145165362341800608157513118689214')
