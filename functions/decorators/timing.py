#!/usr/bin/python

import time
import math

def timer(func):

    def wrapper(*args, **kwargs):

        begin = time.time()

        f = func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

        return f

    return wrapper


@timer
def factorial(num):

    return math.factorial(num)

f = factorial(9580)
print(f)
