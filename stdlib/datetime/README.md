# Date & time 


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


## Format date

Use `strftime` function or f-strings. 

```python
#!/usr/bin/python

from datetime import datetime

now = datetime.now()

print(now.strftime('%d. %b %Y'))
print(f'{now:%d. %b %Y}')
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
from zoneinfo import ZoneInfo
import zoneinfo

# Windows must install tzdata
# pip install tzdata

print(zoneinfo.available_timezones())

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


