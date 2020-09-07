#!/usr/bin/python

import functools

class CountCalls:

    def __init__(self, fun):

        functools.update_wrapper(self, fun)
        self.fun = fun
        self.num_of_calls = 0

    def __call__(self, *args, **kwargs):

        self.num_of_calls += 1
        print(f"Call {self.num_of_calls} of {self.fun.__name__} fun")
        return self.fun(*args, **kwargs)

@CountCalls
def hello():
    print("Hello there!")

hello()
hello()
hello()
