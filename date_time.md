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
from datetime import date
from dateutil.relativedelta import relativedelta

birth_str = '1987-11-08'
born = date.fromisoformat(birth_str)
today = date.today()
age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(age)
```

The solution is harder to read and relies on an implicit transformation.  


## Common datetime formats

```python
from datetime import datetime

now = datetime.now()

# ISO 8601 format (YYYY-MM-DD HH:MM:SS.fff)
iso_8601 = now.isoformat()

# RFC 3339 format (YYYY-MM-DDTHH:MM:SS[.fff]Z) - Zulu time
rfc_3339 = now.isoformat(timespec='seconds') + 'Z'

# US style format (MM-DD-YYYY HH:MM:SS)
us_style = now.strftime("%m-%d-%Y %H:%M:%S")

# European style format (DD/MM/YYYY HH:MM:SS)
european_style = now.strftime("%d/%m/%Y %H:%M:%S")

print("ISO 8601:", iso_8601)
print("RFC 3339:", rfc_3339)
print("US style:", us_style)
print("European style:", european_style)

```


1. **ISO 8601 (YYYY-MM-DD HH:MM:SS.fff)**:
   - This is an international standard (ISO 8601) for representing dates and times. 
   - It uses the extended format YYYY-MM-DD for the date, where YYYY is the four-digit year,  
     MM is the two-digit month (01-12), and DD is the two-digit day (01-31).
   - It uses the 24-hour clock format HH:MM:SS for the time, where HH is the two-digit hour (00-23),  
     MM is the two-digit minutes (00-59), and SS is the two-digit seconds (00-59).
   - Optionally, fractions of a second can be included after the decimal point, denoted by ".fff"  
     where fff represents milliseconds (up to microsecond precision).

2. **RFC 3339 (YYYY-MM-DDTHH:MM:SS[.fff]Z)**:
   - This format is based on ISO 8601 and is defined in RFC 3339, a specification for   
     internet date and time formats.
   - It follows the same date and time format as ISO 8601 (YYYY-MM-DDTHH:MM:SS[.fff]).
   - The key difference is the suffix 'Z' which indicates Coordinated Universal Time (UTC).   
     This specifies that the time is represented in UTC, the primary time standard for the world.  
   - The optional ".fff" again represents fractions of a second.

3. **US style (MM-DD-YYYY HH:MM:SS)**:
   - This format is commonly used in the United States and prioritizes the month over the day.
   - It uses MM-DD-YYYY for the date, where MM is the two-digit month, DD is the two-digit day,  
     and YYYY is the four-digit year.
   - Similar to ISO 8601, it uses the 24-hour clock format HH:MM:SS for the time.

4. **European style (DD/MM/YYYY HH:MM:SS)**:
   - This format is commonly used in many European countries and prioritizes the day over the month. 
   - It uses DD/MM/YYYY for the date, where DD is the two-digit day, MM is the two-digit month, and  
     YYYY is the four-digit year.
   - It follows the same 24-hour clock format HH:MM:SS for the time as the previous formats.

