# Test example


```python
with open('words.txt') as f:

    for line in f:
        print(line.rstrip())
```


```python
def ispunct(c):
    return c in ['!', '.', ',', '?', ';', ':']


msg = "Hello there! How are you? Fine."

n = 0

for c in msg:
    if ispunct(c):
        n = n + 1

print(n)
```

```python
msg = "Hello there! How are you? Fine."

n = 0

for c in msg:
    if c in ['!', '.', ',', '?', ';', ':']:
        n = n + 1  
print(n)
```


```python
vals = (-5, 10, 55, 12, -7, 11, 22)

print(f'minimum je: {min(vals)}')
print(f'maximum je: {max(vals)}')
print(f'pocet prvkov je: {len(vals)}')
print(f'suma je: {sum(vals)}')
```

```python
age_s = input("Enter your age: ")
age = int(age_s)

if age < 18:
    print('minor')
elif age >= 18 and age < 60:
    print('adult')
else:
    print('senior')
```



```python
from random import randint

data = []

for i in range(10):
    r = randint(0, 100)
    data.append(r)

print(f'the sum of random 10 values is {sum(data)}')
```


```python
data = "1,2,3,4,5,6,7,8,9,10"

parts = data.split(',')
print(parts)

mysum = 0

for e in parts:
    mysum = mysum + int(e)

print(mysum)
```


```python
words = ['sky', 'blue', 'cat', 'by', 'cloud', 'an', 'rock', 'pen', 'cup']
words2 = []

for word in words:
    if len(word) == 3 and word.startswith("c"):
        words2.append(word)

print(words2)
```

```python
words = ['sky', 'blue', 'by', 'an', 'rock', 'pen', 'cup']
words2 = []

for word in words:
    if len(word) == 2 or len(word) == 3:
        # print(word)
        words2.append(word)

print(words2)
```


```python
words = ['sky', 'blue', 'by', 'an', 'rock', 'pen', 'cup']

for word in words:
    if len(word) == 2 or len(word) == 3:
        print(word)
```



```python
words = ['sky', 'blue', 'rock', 'pen', 'cup']

print(len(words))

print(words[0])
print(words[-1])
print(words[4])

for word in words:
    print(word, end=" ")

words.sort()

print()

for word in words:
    print(word, end=" ")
```



```python
myname = 'John Doe'
age = 34

print(f"{myname} is {age} years old")
```



## Datetime

```python
#!/usr/bin/python

import datetime

now = datetime.datetime.now()
print(now)

d = datetime.date.today()
print(d)

t = datetime.datetime.now().time()
print(t)
```


```python

vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# while cyklus
# mysum - vysledna sume
# i - pomocna premenna
# len - zisti velkost ntice
```


```python
n_oranges = 12
n_apples = 23

print('There are %d oranges and %d apples in the basket' % (n_oranges, n_apples))
print('There are {0} oranges and {1} apples in the basket'.format(n_oranges, n_apples))
print(f'There are {n_oranges} oranges and {n_apples} apples in the basket')
```

```python

nums = "1,5,6,8,2,3,1,9"

k = nums.split(",")
print(k)

mysum = 0

for e in k:
    mysum = mysum + int(e)

print(e)
```
