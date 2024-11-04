# Priklady


## Read CSV data into namedtuples

```python

from collections import namedtuple
import csv

User = namedtuple('User', 'first_name last_name occupation')

file_name = 'users.csv'
users = []

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    for line in reader:
        user = User(line[0], line[1], line[2])
        users.append(user)


print(users)
```



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

