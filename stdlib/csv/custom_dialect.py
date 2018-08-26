#!/usr/bin/python3

# custom_dialect.py

import csv

csv.register_dialect("hashes", delimiter="#")

f = open('items3.csv', 'w')

with f:

    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pencils", 2)) 
    writer.writerow(("plates", 1))
    writer.writerow(("books", 4))
