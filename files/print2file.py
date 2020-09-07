#!/usr/bin/python

# print2file.py

with open('works.txt', 'w') as f:

    print('Beatrix', file=f)
    print('Honorine', file=f)
    print('The firm of Nucingen', file=f)
