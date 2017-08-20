#!/usr/bin/python3

# read_try_except.py

f = None

try:

    f = open('work.txt', 'r')
    contents = f.readlines()
    print(contents)
    
except IOError as e:

    print(e)    

finally:
    
    if f:
        f.close()
