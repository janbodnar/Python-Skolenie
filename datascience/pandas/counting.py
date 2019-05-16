#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("employees.csv")

print(df.count())

print(f'Number of columns: {len(df.columns)}')

print(df.shape)
