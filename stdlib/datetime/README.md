# Date & time 



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


