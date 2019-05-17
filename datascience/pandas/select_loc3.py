#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("employees.csv")

data = df.loc[(df['Salary'] > 10000) & (df['Salary'] < 50000)]
print(data.head(5))
