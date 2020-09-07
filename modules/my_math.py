
#!/usr/bin/python

"""
A module containing the fibonacci
function.
"""

# my_math.py

def fib(n):

    all = []
    a, b = 0, 1

    while b < n:

        #print (b, end=" ")
        (a, b) = (b, a + b)
        all.extend((a, b))

    return all


# testing

if __name__ == '__main__':
   print (fib(500))
