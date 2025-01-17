#!/usr/bin/python

grades = ['A', 'B', 'C', 'D', 'E', 'F', 'FX']

for grade in grades:

    match grade:
        case 'A' | 'B' | 'C' | 'D' | 'E' | 'F':
            print('passed')
        case 'FX':
            print('failed')


