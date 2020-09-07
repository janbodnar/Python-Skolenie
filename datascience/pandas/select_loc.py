#!/usr/bin/python

import pandas as pd

data = {'Items': ['coins', 'pens', 'books'], 'Quantity': [22, 28, 3]}

df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.loc['A'])

print('-------------------------------')

print(df.loc[['A', 'B'], ['Items']])
