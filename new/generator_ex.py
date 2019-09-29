#!/usr/bin/env python

def countdown():

    num = 0
    print('Starting')

    while True:
        yield num
        num -= 1


max_iter = 3000
i = 0
for val in countdown():
    print(val)       
    i += 1
    if i >= max_iter:
        break 
