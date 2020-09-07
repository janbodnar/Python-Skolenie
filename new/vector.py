#!/usr/bin/python

import math


class Vec2D:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__


u = Vec2D(0, 1)
v = Vec2D(2, 3)
w = Vec2D(-1, 1)

a = u + v
print(a)

print(a == w)

a = u - v
print(a)

a = u * v

print(a)
print(abs(u))
print(u == v)
print(u != v)
