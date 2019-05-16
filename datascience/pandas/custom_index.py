#!/usr/bin/env python3

import pandas as pd

data = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

frame = pd.DataFrame(data)
print(frame)

print('------------------------------')

frame.index = ["BR", "RU", "IN", "CH", "SA"]
print(frame)
