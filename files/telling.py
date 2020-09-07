#!/usr/bin/python

with open('works.txt', 'r') as f:

    print(f'The current file position is {f.tell()}')

    f.read(22)
    print(f'The current file position is {f.tell()}')

    f.seek(0, 0)
    print(f'The current file position is {f.tell()}')
    
