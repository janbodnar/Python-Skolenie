# Samples

```python
vals = [1, 2, -3, -4, 0, 2, 1, 9, 11, -22]

maximum = max(vals)
minimum = min(vals)
n = len(vals)
mysum = sum(vals)

print(f'maximum is {maximum}')
print(f'minimum is {minimum}')
print(f'length is {n}')
print(f'the sum is {mysum}')
```

```python
words = ['sky', 'top', 'warm', 'clear', 'war', 'by', 'net', 'falcon', 'cup']
words_w = []

for word in words:
    if word.startswith('w') or word.startswith('c'):
        words_w.append(word)

print(words)
print(words_w)
```

```python
words = ['sky', 'top', 'warm', 'clear', 'war', 'by', 'net', 'falcon']
words_w = []

for word in words:
    if word.startswith('w'):
        words_w.append(word)

print(words)
print(words_w)
```

```python
words = ['sky', 'top', 'clear', 'by', 'net', 'falcon']
words_3 = []

for word in words:
    if len(word) == 3:
        words_3.append(word)

print(words)
print(words_3)
```


```python
mix = (1, 2, 3, (1, 2, 3, (1, 2, 3, (11, 12, 13))))
print(mix[3][3][3][2])
```


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
