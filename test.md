# Priklady

## Filtering by type

```python
words = []
data = ('sky', 1, 2, True, 'forest', 3.4, 6.7, False, 'water')

for e in data:
    if type(e) == str:
        words.append(e)


print(words)
```


## Floats

```python
# 100 m is 0.1 km

distance = 0.1

# 9.87 s is 9.87/60*60 h

time = 9.87 / 3600

speed = distance / time

print(f"The average speed of a sprinter is {round(speed, 2)} km/h")
print(f"The average speed of a sprinter is {speed} km/h")
```


## Vykonanie operacie x krat

```python
msg = 'hello there!'

i = 1

while i <= 10:
    print(msg)
    i += 1

print('-----------------------')

for i in range(10):
    print(msg)
```


## podmienene vypisovanie slov

`words.txt`:

```
war
sky
cup
cloud
nice
water
warm
```

```python
file_name = 'words.txt'

with open(file_name, 'r') as f:

    lines = f.readlines()
    print(lines)

    for line in lines:

        if line.startswith(('w', 'c')):
            print(line.rstrip())
```


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
