#!/usr/bin/env python3

import pandas as pd

data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print(f'Index: {df.index}')
print(f'Columns: {df.columns}')
print(f'Values: {df.values}')
