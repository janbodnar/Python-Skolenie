# Priklady


## Opakovanie

```python
# vypis hlasku pomocou fstringu
name = 'John Doe'
age = 34
occupation = 'gardener'

msg = f'{name} is {age} years old and he is a {occupation}'
print(msg)


# vypis sumu
# vypis prvy, posledny prvok
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vals[0])
print(vals[-1])

print(sum(vals))

mysum = 0

for val in vals:
    mysum = mysum + val

print(mysum)


# vypocitaj sumu
data = "1,2,3,4,5,6,7,8,9,10"

mysum2 = 0
fields = data.split(',')

for field in fields:
    mysum2 += int(field)

print(mysum2)
```
