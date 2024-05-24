# Date and time

## Today

```python
from datetime import date

today = date.today() 

print(today)

print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)
```

## Current datetime

```python
from datetime import datetime

now = datetime.now()
print(now)
```

## Current datetime in Slovak

Localized datetime for Slovak language.  

```python
import locale
from datetime import datetime

# Set the locale to Slovak
locale.setlocale(locale.LC_TIME, 'sk_SK')

# Get the current datetime
now = datetime.now()

# Print the current date in Slovak
print(now.strftime('%x'))

# Print the current datetime in Slovak
print(now.strftime('%c'))
```



## Calculate age

```python
from datetime import date
from dateutil.relativedelta import relativedelta

birth_str = '1987-11-08'
born = date.fromisoformat(birth_str)
today = date.today()

age = relativedelta(today, born)

print(age.years)
```

The following example utilizes the fact that a boolean `True` evaluates to 1 in the expression.  

```python
birth_str = '1987-11-08'
born = date.fromisoformat(birth_str)
today = date.today()
age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(age)
```

The solution is harder to read and relies on an implicit transformation.  
