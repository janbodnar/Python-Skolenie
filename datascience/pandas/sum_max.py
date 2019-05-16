#!/usr/bin/env python3

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0, 1200, 2), columns=['A'])
# df.index = df.index + 1

print(sum(df['A']))
print(max(df['A']))

# print(df)
