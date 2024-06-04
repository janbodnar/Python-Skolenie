# Code samples

```python
import re

words = [
    "sky.",
    "blue!",
    "falcon  ",
    "\tcloud",
    "book:",
    "small;",
    "nord",
    "car",
    ",ten",
    "atom?",
]


print('------------------------------')
print('for loop')

cleaned = []

for word in words:

    cleaned_word = re.sub(r"[.!,;:?\s]", "", word)
    cleaned.append(cleaned_word)

print(cleaned)

print('------------------------------')
print('list comprehension')

cleaned = [re.sub(r"[.!,;:?\s]", "", word) for word in words]
print(cleaned)


print('------------------------------')
print('map function')

cleaned = list(map(lambda word: re.sub(r"[.!,;:?\s]", "", word), words))
print(cleaned)
```


```python
import sqlite3
from dataclasses import dataclass


@dataclass
class City:
    id: int
    name: str
    population: str


con = sqlite3.connect("test.db")

cities = []

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:

        city = City(*row)
        # city = City(row[0], row[1], row[2])
        cities.append(city)

print(cities)

big_cities = [city for city in cities if city.population > 1000_000]

for bcity in big_cities:
    print(bcity)
```


```python
import requests, re

url = 'https://webcode.me/thermopylae.txt'

resp = requests.get(url)

content = resp.content.decode('utf8')
# print(content)

parts = content.split(' ')
# print(parts)

cleaned = [re.sub(r'[,.\s]', '', e) for e in parts]
print(cleaned)

print(len(cleaned))
print(len(set(cleaned)))
```


```python
import faker
import csv

faker = faker.Faker()

n = 100_000

fname = "users.csv"

with open(fname, 'w') as f:

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['First name', 'Last name', 'Salary'])

    for _ in range(n):

        fname = faker.first_name()
        lname = faker.last_name()
        salary = faker.random_int(850, 3000, 50)

        writer.writerow([fname, lname, salary])
```

---

```python
from dataclasses import dataclass
import csv


@dataclass
class User:
    first_name: str
    last_name: str
    salary: int


fname = 'users.csv'
users = []

with open(fname, 'r') as f:

    reader = csv.reader(f)

    i  = 0

    for row in reader:
        users.append(User(*row))

lastname_w = [ user for user in users if user.last_name.startswith('W') ]

total_salary = sum(int(user.salary) for user in lastname_w)
print(total_salary)


# for user in lastname_w:
#     print(user)

# print(len(lastname_w))
```
