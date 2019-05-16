#!/usr/bin/env python3

import pandas as pd 

df = pd.read_csv("military_spending.csv") 

print(df.to_string(index=False))
