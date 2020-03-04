#!/usr/bin/env python

def uppercase(fun):

    def wrapper():

        res = fun()
        modified = res.upper()

        return modified
    return wrapper


@uppercase
def gen_message():
    return 'Hello there!'

msg = gen_message()
print(msg)
