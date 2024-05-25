# Faker 

`pip install faker`

## Names

```python
from faker import Faker

faker = Faker()

print(f'Name: {faker.name()}')
print(f'First name: {faker.first_name()}')
print(f'Last name: {faker.last_name()}')

print('--------------------------')

print(f'Male name: {faker.name_male()}')
print(f'Female name: {faker.name_female()}')
```

## Jobs

```python
from faker import Faker

faker = Faker()

for _ in range(6):
    print(faker.job())
```

## Localized

```python
from faker import Faker

faker = Faker('cz_CZ')

for i in range(3):

    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()

    print(f'{name}, {address}, {phone}')
```

## Generate CSV data

```python
from faker import Faker
import csv

faker = Faker()

with open('users.csv', 'w', newline='') as f:

    fieldnames = ['id', 'first_name', 'last_name', 'occupation']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1, 101, 1):
        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()

        writer.writerow({'id': _id, 'first_name': fname, 
            'last_name': lname, 'occupation': occupation})
```

## Pick users by last names

```python
import csv 
from collections import namedtuple

User = namedtuple('User', 'id first_name last_name occupation')

fname = 'users.csv'

users = []
users_ab = []

with open(fname) as f:

    reader = csv.reader(f)

    for row in reader:

        u = User(*row)
        users.append(u)

# print(users)
users_ab = [u for u in users if u.last_name.startswith('W') or u.last_name.startswith('A')]

print(len(users_ab))

for u in users_ab:
    print(u)
```
