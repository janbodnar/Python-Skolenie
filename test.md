# Samples


```python
i = 10

while i > 0:
    print('falcon')
    # i += 1
    i = i - 1
```

```python
vals = [-2, 3, 0, 4, -6, 0, 9]

for e in vals:
    if e < 0:
        print(f'{e} is negative')
    elif e == 0:
        print(f'{e} is zero')
    else:
        print(f'{e} is positive')
```



```python
import random


for i in range(5):
    r = random.randint(1, 100)
    msg = f'vygenerovane nahodne cislo: {r}'
    print(msg)
```
