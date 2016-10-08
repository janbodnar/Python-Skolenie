#!/usr/bin/python3

# defining.py

class Some:

    @staticmethod  
    def f():
        print ("f() method")

def f():
    print ("f() function")
    
def g():
    def f():
        print ("f() inner function")
    f()        
        
Some.f()
f()
g()
