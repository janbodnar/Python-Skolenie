# Priklady

## CSV 

reader 

```python
import csv
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    city: str
    salary: int


users = []

with open('users.csv', 'r') as f:

    reader = csv.reader(f)
    
    i = 0

    for row in reader:

        user = User(*row)
        users.append(user)


    print(users[:11])
```


Dictionary reader  

data must contain a header.  

```python
import csv
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    city: str
    salary: int


users = []

with open('users.csv', 'r') as f:

    reader = csv.DictReader(f)
    
    i = 0

    for row in reader:

        user = User(**row)
        users.append(user)


    print(users[:11])
```

## List comprehension

```python
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    city: str
    salary: int


users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    for line in f:
        fields = line.split(',')

        user = User(fields[0], fields[1], fields[2], int(fields[3].rstrip()))
        users.append(user)


    users_a_c = [user for user in users if user.last_name.startswith('A') or user.last_name.startswith('C')]
    users_less_1000 = [user for user in users if user.salary < 1000]

    users_sorted_salary = sorted(users, reverse=True, key=lambda u: u.salary)

for u in users_sorted_salary[:16]:
    print(u)


print(len(users_a_c))
print(users_a_c[0:11])

print('----------------------------')

print(len(users_less_1000))
print(users_less_1000[0:11])
```


## Filter data 

```python
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    city: str
    salary: int

users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    for line in f:
        fields = line.split(',')

        user = User(fields[0], fields[1], fields[2], int(fields[3].rstrip()))
        users.append(user)

    users_w = list(filter(lambda u: u.last_name.startswith('W'), users))
    users_3000 = list(filter(lambda u: u.salary > 3000, users))

print(len(users_w))
print(users_w[0:11])

print('----------------------------')

print(len(users_3000))
print(users_3000[0:11])
```


## Generate test data in CSV

```python
from faker import Faker

faker = Faker()

file_name = 'users.csv'

with open(file_name, 'w') as f:

    for _ in range(100_000):

        fname = faker.first_name()
        lname = faker.last_name()
        city = faker.city()
        salary = faker.random_int(950, 3500)

        line = f'{fname},{lname},{city},{salary}\n'

        f.write(line)
```


## Count vowels, consonants, whitespace

```python

vowels = 0
consonants = 0
punctuations = 0
whitespace = 0
unknown = 0

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in 'aeiouAEIOU':
            vowels += 1
        elif c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            consonants += 1
        elif c in '.!,:,?':
            punctuations += 1
        elif c in ' \n\t':
            whitespace += 1
        else:
            unknown += 1


print(f'vowels: {vowels}')
print(f'consonants: {consonants}')
print(f'whitespace: {whitespace}')
print(f'punctuations: {punctuations}')
print(f'unknown: {unknown}')
```

---

```python
import string

ascii = 0
punctuations = 0
whitespace = 0
unknown = 0

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in string.ascii_letters:
            ascii += 1
        elif c in string.punctuation:
            punctuations += 1
        elif c in string.whitespace:
            whitespace += 1
        else:
            unknown += 1


print(f'ascii: {ascii}')
print(f'whitespace: {whitespace}')
print(f'punctuations: {punctuations}')
print(f'unknown: {unknown}')
```


## Count number of characters in file

```python
letters = {}

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

print(letters)

print(f'The letter a is present {letters['a']} times')
```
