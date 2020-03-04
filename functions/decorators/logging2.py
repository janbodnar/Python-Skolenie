#!/usr/bin/env python

from functools import wraps

def log(fname='output.log'):

    def log_decor(fun):

        @wraps(fun)
        def do_log(*args, **kwargs):

            msg = f'{fun.__name__} was called'
            with open(fname, 'a') as f:
                f.write(msg + '\n')

            return fun(*args, **kwargs)
        return do_log
    return log_decor


@log('data.log')
def power(x):
   return x * x


res = power(4)
print(res)
