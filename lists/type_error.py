#!/usr/bin/python3

# type_error.py

n = [1, 2, 3, 4, 5]

try:
    print (n[1])
    print (n['2'])
    
except TypeError as e:
    
    print ("Error in file %s" % __file__)
    print ("Message: %s" % e)
