# Date and time

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
