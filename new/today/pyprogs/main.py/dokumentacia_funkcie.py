#!/usr/bin/python

# functions in Python are objects

def f():
    """This function prints a message """
    return 'f() function'

print(isinstance(f, object))
print(id(f))
print(f())

print(f.__doc__)
print(f.__name__)