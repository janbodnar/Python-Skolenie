# Code examples


## Pick males/females

pick males/femals from a list of users using list comprehension, records, and  
enumeration.  

```python
from dataclasses import dataclass
from enum import Enum
from collections import namedtuple

Sex = Enum('Sex', ['MALE', 'FEMALE'])


# @dataclass(frozen=True)
# class User:
#     name: str
#     occupation: str
#     sex: Sex

User = namedtuple('User', 'name occupation sex')

users = [User('John Doe', 'gardener', Sex.MALE),
         User('Roger Roe', 'driver', Sex.MALE),
         User('Peter Novak', 'teacher', Sex.MALE),
         User('Lucia Novak', 'teacher', Sex.FEMALE)]

males = [u for u in users if u.sex == Sex.MALE]
females = [u for u in users if u.sex == Sex.FEMALE]

print(males)
print(females)

print(type(males[0]))

for u in males:
    print(u)
```

## Determine weekdays

Determine weekdays from date strings.  

```python
from dateutil import parser
from enum import Enum

data = ['2023-12-23', '2023-5-2', '2023-1-2', '2023-1-1',
        '2023-11-3', '2023-1-23', '2023-8-3', '2023-9-13']

Day = Enum(
    'Day', 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday', start=0)

print(Day.Monday)
print(Day.Tuesday)

print('------------------')

for ds in data:

    dt = parser.parse(ds)
    wd = dt.date().weekday()

    match Day(wd):
        case Day.Monday:
            print('it is', Day.Monday.name)
        case Day.Tuesday:
            print('it is', Day.Tuesday.name)
        case Day.Wednesday:
            print('it is', Day.Wednesday.name)
        case Day.Thursday:
            print('it is', Day.Thursday.name)
        case Day.Friday:
            print('it is', Day.Friday.name)
        case Day.Saturday:
            print('it is', Day.Saturday.name)
        case Day.Sunday:
            print('it is', Day.Sunday.name)
```




