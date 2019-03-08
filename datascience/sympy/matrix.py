#!/usr/bin/env python

from sympy import Matrix, pprint

M = Matrix([[1, 2], [3, 4], [0, 3]])
print(M)
pprint(M)

N = Matrix([2, 2])

print("---------------------------")
print("M * N")
print("---------------------------")

pprint(M*N)
