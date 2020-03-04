#!/usr/bin/env python

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(fun, x):

    res = fun(x)
    return res

x = 2

print(operate(inc, x))
print(x)

print(operate(dec, x))
print(x)

