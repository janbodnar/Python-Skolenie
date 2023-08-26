#!/usr/bin/python

def fn(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

def fn2(a, b, c, *d):
    print(a, b, c, d)

def fn3(a, b, c, *d, e, f):
    print(a, b, c, d, e, f)


vals = [1, 2, 3, 4, 5, 6]

fn(*vals)
fn2(*vals)
fn3(*vals, e=7, f=8)
