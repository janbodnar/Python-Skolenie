#!/usr/bin/python3

# fun_obj.py

def f():
    """This function prints a message """
    print ("Today it is a cloudy day")
    
print (isinstance(f, object))
print (id(f))

print (f.__doc__)
print (f.__name__)
