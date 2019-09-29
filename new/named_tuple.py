#!/usr/bin/env python

from typing import NamedTuple

class Point(NamedTuple):

    x: int
    y: int


p1 = Point(10, 12)
p2 = Point(13, 19)

print(p1)
print(p2)

print(type(p1))
