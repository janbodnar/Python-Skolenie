# List of objects

An object is a grouping of attributes and methods. It can be represented by a  
class/dataclass, namedtuple, or a dictionary.  

- list of dataclass objects
- list of namedtuple objects
- list of dictionaries


Generate a CSV file with faker.  

```python

import csv, random
from faker import Faker 

faker = Faker()
file_name = 'users.csv'

jobs = ['teacher', 'writer', 'programmer', 'shopkeeper', 'driver', 'gardener']

with open(file_name, 'w') as f:

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('first_name', 'last_name', 'country', 'date_of_birth', 'job'))

    for _ in range(30):
        fname = faker.first_name()
        lname = faker.last_name()
        job = random.sample(jobs, 1)[0]
        # job = faker.job()
        dob = faker.date_of_birth()
        country = faker.country()

        writer.writerow((fname, lname, country, dob, job))

```

List of objects created with dataclass or namedtuple.  

```python
import csv
from dataclasses import dataclass
from collections import namedtuple

# @dataclass
# class User:
#     first_name: str
#     last_name: str
#     counry: str
#     date_of_birth: str
#     job: str

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 
for user in users[:11]:
    print(user)
```

List of objects as dictionaries. 

```python
import csv

users = []
file_name = 'users.csv'

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)
    
    i = 1
    for row in reader:
        user = {}
        user['id'] = i
        user.update(row)
        users.append(user)
        i += 1
 
for user in users[:11]:
    print(user)

# print(users)
```

Sort by age 

```python
import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

def calculate_age(dob_str):
    # dob = datetime.strptime(dob_str, "%Y-%m-%d")
    dob = datetime.fromisoformat(dob_str)
    today = datetime.today()
    
    age = relativedelta(today, dob)
    
    return age.years

with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

sorted_users = sorted(users, key=lambda u: calculate_age(u.date_of_birth), 
                      reverse=True)
# sorted_users = sorted(users, key=lambda u: u.date_of_birth)

for user in sorted_users:
    print(user)
```

Using custom method.  

```python
import csv
from datetime import date
from dateutil.relativedelta import relativedelta

from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    counry: str
    date_of_birth: str
    job: str

    def get_age(self):
        born = date.fromisoformat(self.date_of_birth)
        today = date.today()
        age = relativedelta(today, born)
        return age.years    

users = []
file_name = 'users.csv'



with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

sorted_users = sorted(users, key=lambda u: u.get_age(), reverse=True)

for user in sorted_users:
    print(user)
```
