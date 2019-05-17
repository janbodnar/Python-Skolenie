#!/usr/bin/env python3

import pandas as pd

s1 = pd.Series([1, 2, 1, 2, 2, 1, 2, 2])
s2 = pd.Series(['A', 'A', 'B', 'A', 'C', 'C', 'C', 'B'])

data = {'Col 1': s1, 'Col 2': s2}
df = pd.DataFrame(data)

print(df.sort_values(['Col 1', 'Col 2'], ascending=[True, False]))
