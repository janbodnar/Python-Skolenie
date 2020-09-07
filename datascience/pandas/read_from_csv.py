#!/usr/bin/python

import pandas as pd 

df = pd.read_csv("military_spending.csv") 

print(df.to_string(index=False))
