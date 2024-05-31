# Money

A wrapper of `py-moneyed` is used by Django project.  

`pip install py-moneyed`

The `py-moneyed` package in Python offers several advantages over using the `Decimal` class  
for representing monetary values:

1. **Currency and Money Classes**: `py-moneyed` provides `Money` and `Currency` classes, which are more useful for  
   representing instances of money. These classes offer a higher level of abstraction than the `Decimal` class,  
   making it easier to handle money-related operations.  
3. **Avoids Floating Point Issues**: The `Decimal` class is a better choice than floating point numbers for monetary  
   calculations due to precision issues with floats⁴. However, `py-moneyed` takes this a step further by providing  
   dedicated classes for money and currency¹.
5. **Supports Exact Calculations**: `py-moneyed` allows for exact calculations with monetary values, avoiding rounding  
   errors that can occur with chained calculations.  
7. **Ease of Use**: `Money` objects in `py-moneyed` can be used as if they were numbers, providing a  
   straightforward and intuitive interface.
   
In summary, `py-moneyed` offers a more robust and user-friendly way to handle monetary values in Python   
compared to the `Decimal` class.


## List currencies

```python
from moneyed import list_all_currencies

currencies = list_all_currencies()
print(currencies)
print(len(currencies))
```

## Money type

```python
from moneyed import Money


m1 = Money(amount='35.45', currency='EUR')

print(m1.amount)
print(m1.currency)
print(m1.get_amount_in_sub_unit())
```

## Forint 

```python
from moneyed import HUF

print(HUF.get_name(locale='hu_HU'))
print(HUF.get_name(locale='sk_SK'))

print(HUF.code)
print(HUF.name)
```

## Sum Money values

```python
from moneyed import Money, USD

cur = USD

values = (Money('19.99', cur), Money('25.00', cur),
          Money('14.32', cur), Money('6.00', cur))

msum = sum(values)
print(msum)
```



## The get_country_name function

```python
from moneyed import get_country_name
from moneyed import ZMW

print(ZMW.name)


print(get_country_name('ZM', 'en'))
print(get_country_name('ZM', 'ru'))
print(get_country_name('ZM', 'uk'))
print(get_country_name('ZM', 'fr'))
```

---

```python
from moneyed import get_country_name
from moneyed import SKK

print(SKK.name)
print(SKK.code)
print(SKK.numeric)
print(SKK.sub_unit)
print(SKK.countries)

print(get_country_name('SK', 'en'))
print(get_country_name('SK', 'ru'))
print(get_country_name('SK', 'uk'))
print(get_country_name('SK', 'fr'))
```

## Precision

```python
from moneyed import Money


msum = Money(amount='0', currency='EUR')
m = Money(amount='1.46', currency='EUR')

for _ in range(100_000):
    msum += m

print(msum)
print(type(msum))

print('------------------------------')

msum = 0
m = 1.46

for _ in range(100_000):
    msum += m

print(msum)
print(type(msum))
```


