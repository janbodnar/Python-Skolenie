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
