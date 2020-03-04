#!/usr/bin/env python

from functools import wraps

def log(fun):

    @wraps(fun)
    def do_log(*args, **kwargs):

        print(f'{fun.__name__} was called')
        return fun(*args, **kwargs)

    return do_log


@log
def power(x):
   return x * x


res = power(4)
print(res)
