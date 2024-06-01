# Localization 

*Internationalisation* is the process of ensuring that an application is capable of adapting to  
local requirements, for instance ensuring that the local writing system can be displayed.  
*Localisation* is the process of adapting the software to be as familiar as possible to a specific  
locale, by displaying text in the local language and using local conventions for the display of such  
things as units of measurement.


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

## Numbers thousand separator

```python
import locale


val = 111_123_234.25
val2 = "1234567.89"

locale.setlocale(locale.LC_ALL, 'sk_SK')

num = locale.format_string("%d", val, grouping=True) # use thousand separators
print(num)

num2 = locale.atof(val2) # parse
print(num2)

locale.setlocale(locale.LC_ALL, 'en_US')

num = locale.format_string("%d", val, grouping=True) 
print(num)

num2 = locale.atof(val2)
print(num2)
```

## Settings 

```python
import locale

locale.setlocale(locale.LC_ALL, 'sk_SK')

template = """
Numeric formatting:

  Decimal point      : "{decimal_point}"
  Grouping positions : {grouping}
  Thousands separator: "{thousands_sep}"

Monetary formatting:

  International currency symbol   : "{int_curr_symbol!r}"
  Local currency symbol           : {currency_symbol!r}
  Symbol precedes positive value  : {p_cs_precedes}
  Symbol precedes negative value  : {n_cs_precedes}
  Decimal point                   : "{mon_decimal_point}"
  Digits in fractional values     : {frac_digits}
  Digits in fractional values,
                   international  : {int_frac_digits}
  Grouping positions              : {mon_grouping}
  Thousands separator             : "{mon_thousands_sep}"
  Positive sign                   : "{positive_sign}"
  Positive sign position          : {p_sign_posn}
  Negative sign                   : "{negative_sign}"
  Negative sign position          : {n_sign_posn}

"""

sign_positions = {
    0: 'Surrounded by parentheses',
    1: 'Before value and symbol',
    2: 'After value and symbol',
    3: 'Before value',
    4: 'After value',
    locale.CHAR_MAX: 'Unspecified',
}

info = {}
info.update(locale.localeconv())
info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
info['n_sign_posn'] = sign_positions[info['n_sign_posn']]

print(template.format(**info))
```


## Locale switching 

```python
import contextlib
import locale

@contextlib.contextmanager
def temporary_locale(nloc):

    cloc = locale.setlocale(locale.LC_ALL)
    try:
        yield locale.setlocale(locale.LC_ALL, nloc)
    finally:
        locale.setlocale(locale.LC_ALL, cloc)


val = 156_245.99

with temporary_locale('ru_RU'):
    price = locale.currency(val)
    print(price)

with temporary_locale('sk_SK'):
    price = locale.currency(val)
    print(price)
```

## Babel 



```python
from babel import Locale

skl = Locale.parse('sk_SK')

print(skl.get_display_name())
print(skl.get_language_name())
print(skl.get_territory_name())

for e in skl.currencies.values():
    print(e)

for e in skl.currency_symbols.values():
    print(e)
```

## Month/day/quarter names

```python
from babel import Locale

locale = Locale('sk')

month_names = locale.months['format']['wide'].items()
for _, name in month_names:
    print(name)

quars = locale.quarters['format']['wide'].items()
for _, name in quars:
    print(name)

days = locale.days['format']['wide'].items()
for _, name in days:
    print(name)
```

## Numbers/dates/units

```python
from babel.dates import format_date, format_datetime
from babel.numbers import format_decimal, format_percent, parse_decimal
from babel.units import format_unit
from datetime import date, datetime

# Date, time
d = date(2010, 3, 10)
print(format_date(d, format='short', locale='sk'))
print(format_date(d, format='medium', locale='sk'))
print(format_date(d, format='long', locale='sk'))
print(format_date(d, format='full', locale='sk'))
print(format_date(d, "EEEE, d.M.yyyy", locale='sk'))

print('-------------------------------------')

# datetime
dt = datetime.now()
print(format_datetime(dt, "yyyy.MMMM.dd GGG hh:mm a", locale='ru'))
print(format_datetime(dt, "yyyy.MMMM.dd GGG hh:mm a", locale='sk'))

print('-------------------------------------')

# Percents
print(format_percent(0.45, locale='sk'))
print(format_percent(0.45, locale='ru'))
print(format_percent(0.45, locale='fa'))
print(format_percent(0.45, locale='tr'))

print('-------------------------------------')

# Numbers

print(format_decimal(12.4512, locale='sk'))
print(format_decimal(12.4512, locale='ru'))

print('-------------------------------------')

# Units
print(format_unit(16, 'length-meter', locale='ru'))
print(format_unit(16, 'length-meter', locale='en'))
print(format_unit(16, 'length-meter', locale='sk'))
print(format_unit(16, 'length-meter', locale='hu'))
print(format_unit(16, 'length-meter', locale='fr'))
print(format_unit(16, 'length-meter', locale='fa'))

val = parse_decimal('3.229,45', locale='de')
print(val)
```


## Translation


1. Create directories.  

```
md locales\en\LC_MESSAGES
md locales\sk\LC_MESSAGES
```

2. Copy pot files. Add translations

```
cp locales\base.pot locales\en\LC_MESSAGES\base.po
cp locales\base.pot locales\es\LC_MESSAGES\base.po
```

3. Generate final messages.











