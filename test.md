# Priklady

## List comprehensions

```python
negatives = []
positives = []

vals = [0, 2, -2, -9, 11, 9, 8, -3]


for e in vals:
    if e > 0:
        positives.append(e)
    elif e < 0:
        negatives.append(e)


print(positives)
print(negatives)
```


## OOP

```python
#!/usr/bin/python

import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

class Circle:

    def __init__(self, radius=5):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


r = Rectangle(10, 10)
print(r.area())


c = Circle(10)
print(c.area())

c2 = Circle(5)
print(c2.area())

c2.setRadius(1)
print(c2.area())
```


```python
# utils.py

def calculate_max(data):
    return max(data)
    

def calculate_min(data):
    return min(data)

def calculate_sum(data):
    return sum(data)
```

```python
import random
import utils

# main.py

data = []

for i in range(100):
    r = random.randint(-100, 100)
    data.append(r)

maximum = utils.calculate_max(data)
minimum = utils.calculate_min(data)
mysum = utils.calculate_sum(data)


print(f'the maximum of random values is {maximum}')
print(f'the minimum of random values is {minimum}')
print(f'the sum of random values is {mysum}')
```


## recap

```python
data = []

# generate 100 random values (random module)
# create calcuate_max, calculate_min, calculate_sum in utils.py
# use fstrings to generate final output

# --------------------------------

file_name = 'thermopylae.txt'

n_vowels = 0
n_consonants = 0

with open(file_name) as f:
    contents = f.read()
    
    for c in contents:
        
        if c in 'aeiouAEIOU':
            n_vowels += 1
        
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            n_consonants += 1


print(f'there are {n_vowels} vowels')
print(f'there are {n_consonants} consonants')


# --------------------------------

file_name = 'unix-words.txt'

# read the file and calculate the number of all words and 
# the number of words starting with 'w'

file_name = 'unix-words.txt'

all_words = 0
w_words = 0

with open(file_name) as f:

    for word in f:

        all_words += 1
        
        if word.startswith('w') or word.startswith('W'):
            w_words += 1


print(f'there are {all_words} in the file')
print(f'there are {w_words} starting with w/W in the file')

```




## fstring

```python
words = ['sky', 'war', 'cup', 'eleven', 'culminate']

for word in words:
    print(f'{word} has {len(word)} latin characters')
```


## type function

```python
def f():
    pass

data = [1, 2, 3, 4, 'falcon', 3.4, 5.5, True, False, f]

for e in data:
    # if type(e) == int or type(e) == float:
    #     print(e)

    if type(e) in (int, float):
        print(e)
```

```python
def f():
    pass

data = ['war', 'water', 1, 2, 3, 'bar', 4, 'falcon', 3.4, 5.5, True, False, 'warm', f]
w_words = []

for e in data:
    if type(e) == str and e.startswith('w'):
        w_words.append(e)

        
print(w_words)
```


```python
vals = [1, 2, 6, 8, -40, -3]
vals2 = [-4, 45, 11, -7, 11, 0, 18]

mysum = 0

for e in vals:
    mysum += e

for e in vals2:
    mysum += e

print(mysum)
print(sum(vals + vals2))
```

## sum values of vals and vals2

```python
data = '1-2-3-4-5-6-7-8-9-10'

res = data.split('-')
print(res)

mysum = 0

for e in res:
    mysum += int(e)

print(mysum)
```

## calculate sum of numbers

## sum of values in file

```python
filename = 'vals.txt'

mysum = 0

with open(filename, 'r') as f:

    lines = f.readlines()

    for line in lines:
        mysum += int(line.strip())

    print(mysum)
```
