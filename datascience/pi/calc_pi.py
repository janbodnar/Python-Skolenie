#!/usr/bin/python

from decimal import Decimal
from decimal import getcontext

def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range (precision))
print(pi(10))

# precision determines how many digits of pi will be calculated. 
