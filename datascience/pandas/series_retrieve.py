#!/usr/bin/python

import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print(s[0])
print('-----------------------')

print(s[1:4])
print('-----------------------')

print(s[['a','c','d']])
