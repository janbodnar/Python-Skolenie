# Priklady


## Opakovanie

The `users.csv` file:  

```
Tom,Jones,carpenter,2900
John,Doe,gardener,980
Paul,Novak,programmer,2300
Lucy,Smith,teacher,1400
```


```python
# calculate sum
vals = [1, 2, 3, 4, 5]

# calculate number of letters
words = ['sky', 'town', 'nest', 'rock', 'falcon', 'forest']

# calculate the number of vowels
msg = 'there is an old falcon in the sky'


# read users.csv file and create a list of user objects
# using namedtuples

file_name = 'users.csv'
```






## Show Python version and read text file

```python

import sys

print(sys.version)
print(sys.executable)


file_name = 'words.txt'

with open(file_name, 'r') as f:

    for line in f:
        print(line.strip())
```


## list comprehension

```python
vals = [-4, 2, 0, -1, 12, -3]

positive = [e for e in vals if e > 0]
print(positive)

negative = [e for e in vals if e < 0]
print(negative)

words = ['sky', 'ten', 'word', 'tomorrow', 'war', 'pen', 'fly']
words_3 = [word for word in words if len(word) == 3]
print(words_3)
```

```python
words = ['sky', 'ten', 'word', 'tomorrow', 'war', 'pen', 'fly', 'float']
# words_w_f = [word for word in words if word.startswith('w') or word.startswith('f')]
words_w_f = [word for word in words if word.startswith(('w', 'f'))]
print(words_w_f)
```

```python
a = ['a', 2, 1.2, 'c', 12, 3, 'd', 23.4]

b = [e for e in a if type(e) == int]
c = [e for e in a if type(e) == str]
d = [e for e in a if type(e) == float]

print(b)
print(c)
print(d)

float_values = []

for val in a:
    if type(val) == float:
        float_values.append((val))

print(float_values)
```



## filter & map

```python
vals = [1, 2, 3, 4, 5]

vals2 = list(map(lambda e: e * 2, vals))
print(vals2)

vals3 = list(filter(lambda e: e % 2 == 0, vals))
print(vals3)
```



## Read CSV data into namedtuples

```python
from collections import namedtuple
import csv

User = namedtuple('User', 'first_name last_name occupation')

file_name = 'users.csv'
users = []

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    for fields in reader:
        # user = User(fields[0], fields[1], fields[2])
        user = User(*fields)
        users.append(user)


print(users)
```

## Simple namedtuples

```python
from collections import namedtuple

User = namedtuple('User', 'first_name last_name occupation')

u1 = User('John', 'Doe', 'gardener')
# print(u1)

print(f'{u1.first_name} {u1.last_name} is a {u1.occupation}')

u2 = User('Roger', 'Roe', 'driver')
# print(u2)
print(f'{u2.first_name} {u2.last_name} is a {u2.occupation}')
```


```python
def cube(x):
    return x * x * x

c = 5

print(f'The cube of {c} is {cube(c)}')
```


```python
# vypis hlasku pomocou fstringu
name = 'John Doe'
age = 34
occupation = 'gardener'

# vypis prvy, posledny, sumu
vals = [1, 2, -3, -5, 0, 3, 4, 9]

# vypocitaj sumu z cisiel
data = '1,2,3,4,5,6,7,8,9,10'
```


## Riesenie

```python
# vypis hlasku pomocou fstringu
name = 'John Doe'
age = 34
occupation = 'gardener'

msg = f'{name} is {age} years old, he is a {occupation}'
print(msg)

# vypis prvy, posledny, sumu, min, max, velkost
vals = [1, 2, -3, -5, 0, 3, 4, 9]
print(min(vals))
print(max(vals))
print(sum(vals))
print(vals[0])
print(vals[-1])
print(len(vals))


# vypocitaj sumu z cisiel
data = '1,2,3,4,5,6,7,8,9,10'

fields = data.split(',')
print(fields)
mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```

