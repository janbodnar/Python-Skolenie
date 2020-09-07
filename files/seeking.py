#!/usr/bin/python

with open('works.txt', 'r') as f:

    data1 = f.read(22)
    print(data1)

    f.seek(0, 0)

    data2 = f.read(22)
    print(data2)
