#!/usr/bin/python

# write_csv.py

import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

f = open('numbers2.csv', 'w')

with f:

    writer = csv.writer(f)
    
    for row in nms:
        writer.writerow(row)
