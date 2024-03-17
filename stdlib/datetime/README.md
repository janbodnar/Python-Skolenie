# Date & time 

## Current date and time 

```python
#!/usr/bin/python

import datetime

now = datetime.datetime.now()
print(now)

d = datetime.date.today()
print(d)

t = datetime.datetime.now().time()
print(t)
```


## Local & UTC time 

Our planet is a sphere. It revolves round its axis. The Earth rotates towards the east.  
So the Sun rises at different times in different locations. The Earth rotates once in  
about 24 hours. Therefore, the world was divided into 24 time zones. In each time zone,  
there is a different local time. This local time is often further modified by the  
daylight saving.

There is a pragmatic need for one global time. One global time helps to avoid confusion  
about time zones and daylight saving time. The UTC (Universal Coordinated time) was chosen  
to be the primary time standard. UTC is used in aviation, weather forecasts, flight plans,  
air traffic control clearances, and maps. Unlike local time, UTC does not change with  
a change of seasons.

```python
#!/usr/bin/python

from datetime import datetime

print(datetime.now(datetime.UTC))
print(datetime.now())
```

## ISO 8601 format 

## basic format

```python
#!/usr/bin/python

from datetime import datetime

now = datetime.now()
print(now)

iso_date = now.isoformat()
print(iso_date)
```

### various formats

```python
#!/usr/bin/python

from datetime import datetime

fmts = ('2023-11-08', '20231108', '2023-11-08T00:05:23', '2023-11-08T00:05:23Z',
           '20231108T000523', '2023-W01-2T00:05:23.283', '2023-11-08 00:05:23.283',
           '2023-11-08 00:05:23.283+00:00', '2023-11-08T00:05:23+04:00')

for fmt in fmts:
    d = datetime.fromisoformat(fmt)
    print(d, repr(d))
```

### week-numbering format

```python
#!/usr/bin/python

from datetime import datetime

now = datetime.now()
(iso_year, iso_week, _) = now.isocalendar()

iso_fmt = f"{iso_year:-04d}-W{iso_week:02d}-{now.weekday() + 1}"
print(iso_fmt)

d = datetime.fromisoformat(iso_fmt).date()
print(d)
```


## Datetime parts

```python
#!/usr/bin/python

from datetime import datetime
dt = datetime(2023, 9, 15, 22, 3, 31, 355741)

print(f'year: {dt.year}')
print(f'month: {dt.month}')
print(f'hour: {dt.hour}')
print(f'minute: {dt.minute}')
print(f'timestamp: {dt.timestamp()}')
```

## Max/min representable datetimes

```python
#!/usr/bin/python

from datetime import datetime

print(datetime.max)
print(datetime.min)
```

## Unix time 

Unix time is a way of counting time in computers. It represents the number of seconds  
elapsed since midnight (UTC) on January 1st, 1970, which is called the Unix epoch. 


```python
#!/usr/bin/python

import time

print(int(time.time()))
print(time.time())
```

## Timestamp

```python
#!/usr/bin/python

from datetime import date
from time import time

dt = date.fromtimestamp(1568576278)
print(dt)

ts = int(time())
dt2 = date.fromtimestamp(ts)
print(dt2)
```

## Weekday

```python
#!/usr/bin/python

from datetime import datetime

from enum import Enum

class WeekDay(Enum):
    Monday = 0
    Tuesday = 1
    Weekday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    @staticmethod
    def of(val):
        return list(WeekDay)[val]


now = datetime.now()
n = now.weekday()

print(n)
print(WeekDay.of(n))
```

## Day of year

The `toordinal` function returns the *proleptic Gregorian ordinal* value. It refers to a system  
used in the proleptic Gregorian calendar, which extends the Gregorian calendar backward to dates  
preceding its official introduction in 15821. 

In this system, the proleptic Gregorian ordinal of a specific date represents the number of days  
that have elapsed since January 1, 00012. For example, in Python’s datetime module, the `toordinal`    
function returns the proleptic Gregorian ordinal of a specified datetime instance2. This system is  
useful in computer software for identifying pre-Gregorian dates.

```python
#!/usr/bin/python

from datetime import datetime, date

now = datetime.now()
print(now.toordinal())

day_of_year = now.timetuple().tm_yday
print(day_of_year)

day_of_year = now.toordinal() - date(now.year, 1, 1).toordinal() + 1
print(day_of_year)
```


## Comparing dates

We can use relational operators to compare dates.  

```python
#!/usr/bin/python

from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str
    dob: datetime


users = (
    User('John Doe', 'john.doe@example.com', datetime(1985, 8, 21)),
    User('Roger Roe', 'roger.roe@example.com', datetime(1998, 2, 11)),
    User('Paul Anka', 'paul.anka@example.com', datetime(1977, 9, 5)),
    User('Lucia Smith', 'lucia.smith@example.com', datetime(2001, 2, 2)),
    User('Jane Miller', 'jane.miller@example.com', datetime(1967, 5, 15)),
)

oldest = users[0]

for user in users:
    if user.dob < oldest.dob:
        oldest = user

print(oldest)
```


## Format date

Use `strftime` function or f-strings. 

```python
#!/usr/bin/python

from datetime import datetime

now = datetime.now()

print(now.strftime('%d. %b %Y'))
print(f'{now:%d. %b %Y}')
```

## Get age

```python
#!/usr/bin/python


from datetime import date


def calculate_age(born):

    today = date.today()
    # return today.year - born.year - (today.timetuple()[1:3] < born.timetuple()[1:3])
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


d1 = date(2002, 3, 12)
print(f'{calculate_age(d1)}')

d2 = date(1977, 3, 17)
print(f'{calculate_age(d2)}')
```



## Difference in days

```python
#!/usr/bin/python

from datetime import date

d0 = date(2018, 8, 15)
d1 = date(2018, 9, 26)

delta = d1 - d0
print(delta.days)
```

## Timezones

```python
#!/usr/bin/python

from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

# Windows must install tzdata
# pip install tzdata

print(available_timezones())

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_MSC = ZoneInfo('Europe/Moscow')
datetime_Moscow = datetime.now(tz_MSC)
print("Moscow:", datetime_Moscow.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = ZoneInfo('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
```

## Days until XMas

```python
#!/usr/bin/python

from datetime import datetime

now = datetime.now()
xmas = datetime(now.year, 12, 25)
delta = xmas - now
final = delta.days

if final > 0:
    print(final, "days until XMas")
elif final == 0:
    print("Merry XMas!")
elif final < 0:
    print("It is past XMas, wait until next year!")
```

## Parsing date & time

We use the `strptime` function to parse datetime objects from strings.  

```python
#!/usr/bin/python

from datetime import datetime

dt1 = datetime.strptime('Jun 1 2018 5:33PM', '%b %d %Y %I:%M%p')
print(dt1)

dt2 = datetime.strptime('23:33:45', '%H:%M:%S')
print(dt2.time())
```

## Time deltas 

```python
#!/usr/bin/python

import datetime

now = datetime.datetime.now()
print(now)

dt1 = now + datetime.timedelta(days=1, hours=2)
print(dt1)

dt2 = now - datetime.timedelta(weeks=9)
print(dt2)
```


