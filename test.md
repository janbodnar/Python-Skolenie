# Priklady 13.11.24

## Opakovanie

```python

# calculate sum
vals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

mysum = 0

for nested in vals:
    mysum += sum(nested)

print(mysum)


# generate a list of 100 random numbers and calculate its sum

import random

random_vals = []

for _ in range(100):
    r = random.randint(0, 100)
    random_vals.append(r)

print(len(random_vals))
print(sum(random_vals))



# generate list of words starting with c or w
data = """
sky
down
cup
blue
python
dark
war
water
roam
club
"""

fields = data.splitlines()[1:]
# fields.pop(0)

words_w_c = [field for field in fields if field.startswith(('w', 'c'))]
print(words_w_c)
```
