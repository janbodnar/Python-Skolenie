#!/usr/bin/python

# returning2.py

n = [1, 2, 3, 4, 5]

def stats(x):

    mx = max(x)
    mn = min(x)
    ln = len(x)
    sm = sum(x)
    
    return mx, mn, ln, sm    
    
mx, mn, ln, sm = stats(n)
print (stats(n))

print (mx, mn, ln, sm)
