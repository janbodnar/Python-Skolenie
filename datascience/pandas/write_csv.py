#!/usr/bin/env python3

import pandas as pd 

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

df.to_csv("users.csv", index=False) 
