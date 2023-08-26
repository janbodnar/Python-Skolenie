#!/usr/bin/python

def do_sum(*args):
   '''Function returns the sum 
   of all values'''
   
   r = 0
   
   for i in args:
      r += i
      
   return r


print(do_sum.__doc__)
print(do_sum(1, 2, 3))
print(do_sum(1, 2, 3, 4, 5))
