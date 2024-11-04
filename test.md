# Priklady

```python
# vypis hlasku pomocou fstringu
name = 'John Doe'
age = 34
occupation = 'gardener'

# vypis prvy, posledny, sumu
vals = [1, 2, -3, -5, 0, 3, 4, 9]

# vypocitaj sumu z cisiel
data = '1,2,3,4,5,6,7,8,9,10'
```


## Riesenie

```python
# vypis hlasku pomocou fstringu
name = 'John Doe'
age = 34
occupation = 'gardener'

msg = f'{name} is {age} years old, he is a {occupation}'
print(msg)

# vypis prvy, posledny, sumu, min, max, velkost
vals = [1, 2, -3, -5, 0, 3, 4, 9]
print(min(vals))
print(max(vals))
print(sum(vals))
print(vals[0])
print(vals[-1])
print(len(vals))


# vypocitaj sumu z cisiel
data = '1,2,3,4,5,6,7,8,9,10'

fields = data.split(',')
print(fields)
mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```

