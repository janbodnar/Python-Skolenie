#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("military_spending.csv")

print(df.sample(3))
