# Priklady

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


def by_age(u):

    age = calculate_age(u.date_of_birth)
    return age <= 30


with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

users_20_24 = list(filter(by_age, users))

print(users_20_24)
```
