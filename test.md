# Priklady

## Filter by type

```python
data = ['falcon', 1, 2, 0, True, 4.5, (1, 2, 3), False, 6.7, 9.0, None]

for e in data:
    if type(e) == bool:
        print(e)
```

## Using f descriptor as iterator

```python
words_w_c = []

file_name = 'words.txt'

with open(file_name, 'r') as f:

    for line in f:

        if line.startswith('w') or line.startswith('c'):
            words_w_c.append(line.strip())

    print(words_w_c)
```


## Reading words into list

```python
words_w_c = []

file_name = 'words.txt'

with open(file_name, 'r') as f:

    lines = f.readlines()
    for line in lines:

        if line.startswith('w') or line.startswith('c'):
            words_w_c.append(line.strip())

    print(words_w_c)
```


```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
print(mix[3][3][3][1])
```

```python
file_name = 'data.csv'

with open(file_name, 'r') as f:

    lines = f.readlines()

    for line in lines:
        fields = line.split(",")
        # print(fields)

        speed = float(fields[0]) / float(fields[1].strip())
        print(f'The average speed is {speed:.3} km/h')
```


```python
distance = float(input("Enter distance in km: "))
time = float(input("Enter time in h: "))

speed = distance / time

print(f"The average speed of a sprinter is {speed} km/h")
```



Zadanie:  

```python
# sumu, pocet prvkov, min, maximum
# vypis 1. a posledny provok
vals = (1, 2, 3, 4, 5, 6, 7)

# vypis hlasku John Doe is a gardener pomocou fstringu
data = 'John,Doe,gardener'

# vypis hlasky pomocou fstringu pre vsetkych
data2 = '''
John,Doe,gardener
Roger,Roe,driver
Lucia,Smith,teacher
'''
```

Riesenie: 

```python

# sumu, pocet prvkov, min, maximum
# vypis 1. a posledny provok
vals = (1, 2, 3, 4, 5, 6, 7)

print(sum(vals))
print(min(vals))
print(max(vals))
print(vals[0])
print(vals[-1])

prvy = vals[0]
print(prvy)

# vypis hlasku John Doe is a gardener pomocou fstringu
data = 'John,Doe,gardener'

fields = data.split(",")
print(f'{fields[0]} {fields[1]} is a {fields[2]}')

# vypis hlasky pomocou fstringu pre vsetkych
data2 = '''John,Doe,gardener
Roger,Roe,driver
Lucia,Smith,teacher
'''

lines = data2.splitlines()
print(lines)

for line in lines:
    fields = line.split(",")
    # print(fields)
    print(f'{fields[0]} {fields[1]} is a {fields[2]}')
```


```python
file_name = 'words.txt'

with open(file_name) as f:

    lines = f.readlines()

    for word in lines:
        print(f'{word.rstrip()} has {len(word.rstrip())} characters')
```

```python
# first_name = 'John'
# last_name = 'Doe'
# occupation = 'gardener'

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
occupation = input("Enter your occupation: ")


# msg = first_name + ' ' + last_name + " is a " + occupation
msg = f'User {first_name} {last_name} is a {occupation}'

print(msg)
```


```python
file_name = 'words.txt'

with open(file_name) as f:

    lines = f.readlines()
    # print(lines)

    for line in lines:

        if line.startswith('w') or line.startswith('c') :
            print(line.rstrip())
```


```python
nums = "1,5,6,8,2,3,1,9"
fields = nums.split(",")

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```


```python
name = 'Peter'
age = 23
occupation = 'programmer'

print('%s is %d years old and he is a %s' % (name, age, occupation))
print('{} is {} years old and he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old and he is a {occupation}')
```


```python
word = 'falcon'

i = 1

while i <= 10:

    print(f'{i}. {word}')
    i = i + 1

print('end of program')
```


```python
# vals = [1, 2, 2, 3, 3, 4, 5, 6]
#
# print(vals)
# print(vals[0])
# print(vals[1])
# print(vals[3])
# print(vals[7])
#
# print(vals[-1])
# print(vals[-2])

words = ['sky', 'atom', 'new', 'war', 'cloud', 'pen']

print(words[0])
print(words[-1])
print(len(words))
# print(sum(words))
```

```python
name = "John Doe"
age = 23
occupation = 'gardener'

print(name, age, occupation)

print(type(name))
print(type(age))
```


```python
vals = [1, 2, 2, 3, 3, 4, 5, 6]

print(vals)
print(sum(vals))
print(len(vals))
print(len(occupation))
```
