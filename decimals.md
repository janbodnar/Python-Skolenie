# Decimal 

High-precision calculation in Python with `Decimal` type. The type is  
located in the `decimal` module. 

The Python decimal module provides support for fast correctly-rounded  
decimal floating point arithmetic. 

By default, Python interprets any number that includes a decimal point  
as a double precision floating point number. The Decimal is a floating  
decimal point type which more precision and a smaller range than the float.  
It is appropriate for financial and monetary calculations. It is also  
closer to the way how humans work with numbers.  

Unlike hardware based binary floating point, the decimal module has  
a user alterable precision which can be as large as needed for  
a given problem. The default precision is 28 places. 

Some values cannot be exactly represented in a float data type.  
For instance, storing the 0.1 value in float (which is a binary floating point value)     
variable we get only an approximation of the value. Similarly, the 1/3 value  
cannot be represented exactly in decimal floating point type. 

## Float imprecision

```python
#!/usr/bin/python

n1 = 0.6
n2 = 0.7

print(n1 + n2)
```

## Default precision 

The Decimal has a default precision of 28 places, while the float has 18 places. 

```python
#!/usr/bin/python

from decimal import Decimal

x = 1 / 3
print(type(x))
print(x)

print("-----------------------")

y = Decimal(1) / Decimal(3)
print(type(y))
print(y)
```

## Comparing

Caution should be exercised when comparing floaing point values. While in many  
real world problems a small error is negligible, financial and monetary  
calculations must be exact.

```python
#!/usr/bin/python

from decimal import Decimal

x = 0.1 + 0.1 + 0.1

print(x == 0.3)
print(x)

print("----------------------")

x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')

print(x == Decimal('0.3'))
print(float(x) == 0.3)
print(x)
```

## Altering precision

We can change the default precision of the Decimal type.  
The mpmath module is a library for arbitrary-precision  
floating-point arithmetic.

`$ pip install mpmath`

we change the precision to 50 places. We compare the accuracy  
of the math.sqrt, Decimal's sqrt, and mpmath.sqrt functions. 

```python
#!/usr/bin/python

from decimal import Decimal, getcontext
import math

import mpmath

getcontext().prec = 50
mpmath.mp.dps = 50
num = Decimal(1) / Decimal(7)

num2 = mpmath.mpf(1) / mpmath.mpf(7)

print('   math.sqrt: {0}'.format(Decimal(math.sqrt(num))))
print('decimal.sqrt: {0}'.format(num.sqrt()))
print(' mpmath.sqrt: {0}'.format(mpmath.sqrt(num2)))
print('actual value: 0.3779644730092272272145165362341800608157513118689214')
```

## Rounding 

The Decimal type provides several rounding options:

- ROUND_CEILING - always round upwards towards infinity
- ROUND_DOWN - always round toward zero
- ROUND_FLOOR - always round down towards negative infinity
- ROUND_HALF_DOWN - rounds away from zero if the last significant  
  digit is greater than or equal to 5, otherwise toward zero
- ROUND_HALF_EVEN - like ROUND_HALF_DOWN except that if the value  
  is 5 then the preceding digit is examined; even values cause the  
  result to be rounded down and odd digits cause the result to be rounded up.
- ROUND_HALF_UP - like ROUND_HALF_DOWN except if the last significant  
  digit is 5 the value is rounded away from zero
- ROUND_UP - round away from zero
- ROUND_05UP - round away from zero if the last digit is 0 or 5, otherwise towards zero


```python
#!/usr/bin/python

import decimal

context = decimal.getcontext()

rounding_modes = [
    'ROUND_CEILING',
    'ROUND_DOWN',
    'ROUND_FLOOR',
    'ROUND_HALF_DOWN',
    'ROUND_HALF_EVEN',
    'ROUND_HALF_UP',
    'ROUND_UP',
    'ROUND_05UP',
    ]

col_lines = '-' * 10

print(f"{' ':20} {'1/7 (1)':^10} {'1/7 (2)':^10} {'1/7 (3)':^10} {'1/7 (4)':^10}")
print(f"{' ':20} {col_lines:^10} {col_lines:^10} {col_lines:^10} {col_lines:^10}")

for mode in rounding_modes:

    print(f'{mode:20}', end=' ')

    for precision in [1, 2, 3, 4]:

        context.prec = precision
        context.rounding = getattr(decimal, mode)
        value = decimal.Decimal(1) / decimal.Decimal(7)
        print(f'{value:<10}', end=' ')
    print()

print('********************************************************************')

print(f"{' ':20} {'-1/7 (1)':^10} {'-1/7 (2)':^10} {'-1/7 (3)':^10} {'-1/7 (4)':^10}")
print(f"{' ':20} {col_lines:^10} {col_lines:^10} {col_lines:^10} {col_lines:^10}")


for mode in rounding_modes:

    print(f'{mode:20}', end=' ')

    for precision in [1, 2, 3, 4]:

        context.prec = precision
        context.rounding = getattr(decimal, mode)
        value = decimal.Decimal(-1) / decimal.Decimal(7)
        print(f'{value:<10}', end=' ')

    print()
```
```
                      1/7 (1)    1/7 (2)    1/7 (3)    1/7 (4)
                     ---------- ---------- ---------- ----------
ROUND_CEILING        0.2        0.15       0.143      0.1429
ROUND_DOWN           0.1        0.14       0.142      0.1428
ROUND_FLOOR          0.1        0.14       0.142      0.1428
ROUND_HALF_DOWN      0.1        0.14       0.143      0.1429
ROUND_HALF_EVEN      0.1        0.14       0.143      0.1429
ROUND_HALF_UP        0.1        0.14       0.143      0.1429
ROUND_UP             0.2        0.15       0.143      0.1429
ROUND_05UP           0.1        0.14       0.142      0.1428
********************************************************************
                      -1/7 (1)   -1/7 (2)   -1/7 (3)   -1/7 (4)
                     ---------- ---------- ---------- ----------
ROUND_CEILING        -0.1       -0.14      -0.142     -0.1428
ROUND_DOWN           -0.1       -0.14      -0.142     -0.1428
ROUND_FLOOR          -0.2       -0.15      -0.143     -0.1429
ROUND_HALF_DOWN      -0.1       -0.14      -0.143     -0.1429
ROUND_HALF_EVEN      -0.1       -0.14      -0.143     -0.1429
ROUND_HALF_UP        -0.1       -0.14      -0.143     -0.1429
ROUND_UP             -0.2       -0.15      -0.143     -0.1429
ROUND_05UP           -0.1       -0.14      -0.142     -0.1428
```

## Fractions 

The `fractions` module provides support for rational number arithmetic. 

```python
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
```

## Example

In the example, we increase the price by 13% and calculate the sum of  
the value of all beverages.  

```python
#!/usr/bin/python

# from products2 import get_products
from products import get_products
from decimal import Decimal

data = get_products()

res = [p for p in data if p.category == 'Beverages']
print(len(res))

val = sum(p.unit_price * p.units_in_stock for p in res)
print(val)

# d = 1.13
# val = sum(p.unit_price * d * p.units_in_stock for p in res)
# print(val)

d = 1.13
val = sum(p.unit_price * Decimal(str(d)) * p.units_in_stock for p in res)
print(val)
```

There is a small error if we use floats.  

```
$ ./increase.py
12
12480.25
14102.682499999997

$ ./increase.py
12
12480.25
14102.6825
```


