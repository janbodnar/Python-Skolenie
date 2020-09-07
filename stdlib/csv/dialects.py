#!/usr/bin/python

# dialects.py

import csv

names = csv.list_dialects()

for name in names:
    
    print(name)
    
    dialect = csv.get_dialect(name)
    
    print(repr(dialect.delimiter), end=" ")
    print(dialect.doublequote, end=" ")
    print(dialect.escapechar, end=" ")
    print(repr(dialect.lineterminator), end=" ")
    print(dialect.quotechar, end=" ")
    print(dialect.quoting, end=" ")
    print(dialect.skipinitialspace, end=" ")
    print(dialect.strict)
