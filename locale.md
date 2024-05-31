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
