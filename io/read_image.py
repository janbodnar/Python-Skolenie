#!/usr/bin/python

import binascii
from more_itertools import sliced

# sudo pip3 install more_itertools

with open('sid.jpg', 'rb') as f:

    content = f.read()
    hexed = binascii.hexlify(content)
    # print(hexed)
    mybytes = list(sliced(hexed, 2))

    i = 0
    for b in mybytes:
        print(b.decode("utf-8") , end=' ')
        i += 1
        if (i % 30 == 0):
            print()
