#!/usr/bin/env python

# uses matplotlib

from sympy import symbols, cos
from sympy.plotting import plot3d

x, y = symbols('x y')
plot3d(cos(x*3)*cos(y*5)-y)
