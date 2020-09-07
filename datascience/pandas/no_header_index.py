#!/usr/bin/python

import pandas as pd 
  
df = pd.read_csv("military_spending.csv") 

print(df.head(4).to_string(header=False, index=False))
