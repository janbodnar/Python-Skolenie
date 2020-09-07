#!/usr/bin/python

import pandas as pd

df = pd.read_csv("employees.csv")

# integer-location based indexing for selection by position.
# Multiple row and column selections using iloc and DataFrame

print(df.iloc[0:6])  # first six rows of dataframe
print('--------------------------------------')

print(df.iloc[:, 0:2])  # first two columns of data frame with all rows
print('--------------------------------------')

# 1st, 4th, 7th, 25th row + 1st 6th 8th column
print(df.iloc[[0, 3, 6, 24], [0, 5, 7]])
print('--------------------------------------')

# first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).
print(df.iloc[:5, 5:8])
print('--------------------------------------')
