#!/usr/bin/python

# fun_coll.py

def f():
    pass

def g():
    pass
  
def h(f):
    print (id(f))
  
a = (f, g, h)

for i in a:
    print (i)
    
h(f)
h(g)
