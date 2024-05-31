# Localization 

```python
import locale

vals = [12_345, 234.345, 12.56]

locale.setlocale(locale.LC_ALL, 'fr_FR')

for val in vals:
    num = locale.format_string("%.2f", val)
    print(num)

locale.setlocale(locale.LC_ALL, 'us_US')

for val in vals:
    num = locale.format_string("%.2f", val)
    print(num)

locale.setlocale(locale.LC_ALL, 'fa_IR')

for val in vals:
    num = locale.format_string("%.2f", val)
    print(num)
```

## Dates

```python
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')

fmt = "%A, %d %B %Y - %H:%M"
now = datetime.datetime.now()

fdt = now.strftime(fmt)
print(fdt)

locale.setlocale(locale.LC_ALL, 'sk_SK')

fdt = now.strftime(fmt)
print(fdt)

locale.setlocale(locale.LC_ALL, 'ru_RU')

fdt = now.strftime(fmt)
print(fdt)

locale.setlocale(locale.LC_ALL, 'hu_HU')

fdt = now.strftime(fmt)
print(fdt)
```
