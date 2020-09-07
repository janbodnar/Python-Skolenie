#!/usr/bin/python

with open('web.png', 'rb') as f:

    hexdata = f.read().hex()
    
    n = 2
    data = [hexdata[i:i+n] for i in range(0, len(hexdata), n)]

    i = 0
    for e in data:

        print(e, end=' ')
        i += 1

        if i % 20 == 0:
            print()

    print()
