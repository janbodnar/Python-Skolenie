#!/usr/bin/python

import pandas as pd

s1 = pd.Series([2, 1, 4, 5, 3, 8, 7, 6])
s2 = pd.Series([12, 23, 31, 14, 11, 61, 17, 18])

data = {'Col 1': s1, 'Col 2': s2}
df = pd.DataFrame(data)

print(df.sort_values('Col 1', ascending=True))
print('------------------------------------')
print('Sorted')

print(df.sort_values('Col 2', ascending=False))
