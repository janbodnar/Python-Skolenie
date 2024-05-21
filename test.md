# Samples

```python
def starts_w(e):
    return e.startswith('w')

def starts_w_o(e):
    return e.startswith('w') or e.startswith('o')

words = ['sky', 'war', 'water', 'cup', 'ocean', 'owl']

data = list(filter(starts_w, words))
print(data)

data = list(filter(starts_w_o, words))
print(data)
```


```python
vals = (1, 2, 3, 7, 8, 11, 12, -6, -21, 22)
evens = []
odds = []

for val in vals:
    if val % 2 == 0:
        evens.append(val)
        
print(evens)

for val in vals:
    if val % 2 == 1:
        odds.append(val)

print(odds)
```



```python
nums = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

for i in nums:
    for e in i:
        for f in e:
            print(f)
```



```python
data = '1-2-3-4-5-6-7-8-9-10'
mysum = 0

substrings = data.split('-')
print(substrings)

for val in substrings:
    mysum += int(val)

print(mysum)
```


```python
words = ['sky', 'cup', 'blue', 'bottom', 'war', 'atom', 'water', 'car']
words_w = []
words_w_c = []

for word in words:
    if word.startswith('w'):
        words_w.append(word)

print(words_w)


for word in words:
    if word.startswith('w') or word.startswith('c'):
        words_w_c.append(word)

print(words_w_c)
```


```python

words = ['sky', 'blue', 'bottom', 'war', 'atom', 'water', 'car']

for word in words:
    print(word)

for word in words:
    print(word, end=' ')

print()

for word in words:
    print(word.capitalize(), end=' ')
```


```python
age_s = input('Enter your age: ')
age = int(age_s)

if age < 18:
    print('minor')
# elif age >= 18 and age < 70:
elif 18 <= age < 70:
    print('adult')
else:
    print('senior')
```


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
