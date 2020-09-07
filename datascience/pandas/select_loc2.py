#!/usr/bin/python

import pandas as pd

data = {'Items': ['coins', 'pens', 'books'], 'Quantity': [22, 28, 3]}

df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.loc[[True, False, True], ['Items', 'Quantity']])
