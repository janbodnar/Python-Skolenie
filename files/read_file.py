#!/usr/bin/python

# redirect.py

import sys

with open('output.txt', 'w') as f:
    
    sys.stdout = f

    print('Lucien')
    sys.stdout.write('Rastignac\n')
    sys.stdout.writelines(['Camusot\n', 'Collin\n'])

    sys.stdout = sys.__stdout__

    print('Bianchon')
    sys.stdout.write('Lambert\n')
