#!/usr/bin/python

class Math:

    @staticmethod
    def abs(x):

        if x < 0:
            return -x
        return x


print(Math.abs(3))
print(Math.abs(-3))
