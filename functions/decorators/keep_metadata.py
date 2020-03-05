#!/usr/bin/env python

from functools import wraps

def enclose(fun):

    @wraps(fun)
    def wrapper():
        '''This is wrapper function'''

        print("***************************")
        fun()
        print("***************************")

    return wrapper

@enclose
def myfun():
    '''this is myfun()''' 
    print("myfun")

myfun()

print(myfun.__name__)
print(myfun.__doc__)
