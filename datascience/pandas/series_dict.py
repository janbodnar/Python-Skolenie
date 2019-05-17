#!/usr/bin/env python3

import pandas as pd
import numpy as np

data = {'coins' : 22, 'pens' : 3, 'books' : 28}
s = pd.Series(data)

print(s)

# print(s.to_string(index=False))
