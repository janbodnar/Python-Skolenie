#!/usr/bin/env python

import pandas as pd 
  
df = pd.read_csv("military_spending.csv") 

print(df.head(4))

print('*******************************************')

print(df.tail(4))
