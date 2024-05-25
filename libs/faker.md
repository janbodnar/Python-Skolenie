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

## Date and time 

```python
from faker import Faker

faker = Faker()

print(f'Date of birth: {faker.date_of_birth()}')
print(f'Century: {faker.century()}')
print(f'Year: {faker.year()}')
print(f'Month: {faker.month()}')
print(f'Month name: {faker.month_name()}')
print(f'Day of week: {faker.day_of_week()}')
print(f'Day of month: {faker.day_of_month()}')
print(f'Time zone: {faker.timezone()}')
print(f'AM/PM: {faker.am_pm()}')
```

---

```python
from faker import Faker

faker = Faker()

print(f'Datetime this century: {faker.date_time_this_century()}')
print(f'Datetime this decade: {faker.date_time_this_decade()}')
print(f'Datetime this year: {faker.date_time_this_year()}')
print(f'Datetime this month: {faker.date_time_this_month()}')

print('-------------------------')

print(f'Date this century: {faker.date_this_century()}')
print(f'Date this decade: {faker.date_this_decade()}')
print(f'Date this year: {faker.date_this_year()}')
print(f'Date this month: {faker.date_this_month()}')

print('-------------------------')

TOTAL_SECONDS = 60*60*24*2 # two days

series = faker.time_series(start_date='-12d', end_date='now', precision=TOTAL_SECONDS)

for val in series:
    print(val[0])
```

---

```python
from faker import Faker

faker = Faker()

print(f'Unix time: {faker.unix_time()}')
print(f'Datetime: {faker.date_time()}')
print(f'iso8601: {faker.iso8601()}')
print(f'Date: {faker.date()}')
print(f'Time: {faker.time()}')

print('-------------------------')

print(f"Datetime between: {faker.date_time_between(start_date='-15y', end_date='now')}")
print(f"Date between: {faker.date_between()}")

print('-------------------------')

print(f"Future datetime: {faker.future_datetime()}")
print(f"Future date: {faker.future_date()}")
print(f"Past datetime: {faker.past_datetime()}")
print(f"Past date: {faker.past_date()}")
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
