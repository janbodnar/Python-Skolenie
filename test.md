# Priklady

```python

# calculate sum
vals = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

mysum = 0

# for val in vals:
#     mysum += sum(val)

for nested in vals:
    for val in nested:
        mysum += val

print(mysum)


# generate a list of 100 random numbers 0-100 and calculate its sum
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

lines = data.splitlines()[1:]

words_c_w = [line for line in lines if line.startswith('w') or line.startswith('c')]
print(words_c_w)


# words_c_w = []
# for line in lines:
#     if line.startswith('w') or line.startswith('c'):
#         words_c_w.append(line)

# print(words_c_w)
```
