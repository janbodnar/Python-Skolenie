# Priklady

## Filtering users in file

```python
file_name = 'users.csv'

all = []
users_w = []

with open(file_name, 'r') as f:

    for line in f:
        fields = line.rstrip().split(',')
        all.append(fields)
        if fields[1].startswith('W'):
            users_w.append(fields)


    print(users_w)

    filtered = list(filter(lambda x: x[1].startswith('W'), all))
    # filtered = list(filter(lambda x: x[1][0] == 'W', all))
    print(filtered)

    print(users_w == filtered)
```


```python
import faker

faker = faker.Faker()

first_name = faker.first_name()
last_name = faker.last_name()
city = faker.city()
state = faker.state()
email = faker.email()

print(first_name, last_name, city, state, email)

file_name = 'users.csv'

with open(file_name, 'w') as f:
    f.write('first_name,last_name,city,state,email\n')
    for _ in range(1000):
        first_name = faker.first_name()
        last_name = faker.last_name()
        city = faker.city()
        state = faker.state()
        email = faker.email()

        f.write(f'{first_name},{last_name},{city},{state},{email}\n')
```


## Lambda functions

```python
# map
# filter

# negative_vals = []

vals = [-3, 4, 0, 2, -1, 0, 9, -9]

# def is_negative(e):
#     if e < 0:
#         return True

# def is_negative(e):
#     if e < 0:
#         return True


def is_positive(e):
    return e > 0


# for val in vals:
#     if val < 0:
#         negative_vals.append(val)

neg_vals = list(filter(lambda e: e < 0, vals))
print(neg_vals)

pos_vals = list(filter(lambda e: e > 0, vals))
print(pos_vals)
```


```python
words = ['apple', 'cup', 'war', 'banana', 'cherry', 'date', 'water', 'elderberry', 'fig', 'grape']

# def starts_with_w(word):
#     if word[0] == 'w':
#         return True
    # return word[0] == 'w'

# words_w = list(filter(starts_with_w, words))
# print(words_w)

# words_w_c = list(filter(lambda word: word[0] == 'w' or word[0] == 'c', words))
words_w_c = list(filter(lambda word: word[0] in ('w', 'c'), words))
print(words_w_c)

# words_w = list(filter(lambda w: w[0] == 'w', words))
# print(words_w)
```

```python
def twice(x):
    return x * 2

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# vals2 = list(map(twice, vals))
vals2 = list(map(lambda e: e * 2, vals))

print(vals2)
print(vals)
```

```python
# sum vals
data = '1,2,3,4,5,6,7,8,9,10'

fields = data.split(',')
mysum = sum(map(int, fields))
print(mysum)
```



## Opakovanie


```python
# print message John Doe is a gardener and live in 
# in New York
name = 'John Doe'
occupation = 'gardener'
city = 'New York'


# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

# calculate sum
data2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10))

# create a new tuple that contains words starting with w or c
words = ['small', 'cup', 'war', 'water', 'cloud', 'warm', 'atom']

# read file words.txt and calculate the number 
# of all ascii characters of all words
```

```
sky
blue
red
brown
pen
dog
forest
```

Riesenie:

```python

# 3916 prezencne

# print message John Doe is a gardener and live in 
# in New York
name = 'John Doe'
occupation = 'gardener'
city = 'New York'

msg = f'{name} is a {occupation} and lives in {city}'
print(msg)


# calculate sum
# split, int
data = "1,2,3,4,5,6,7,8,9,10"

mysum = 0
fields = data.split(',')

print(fields)

for field in fields:
    mysum += int(field)

print(mysum)


# calculate sum
mysum2 = 0
data2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))

for nested in data2:
    for e in nested:
        mysum2 += e

print(mysum2)

# create a new tuple that contains words starting with w or c
# startswith
words = ['small', 'cup', 'war', 'water', 'cloud', 'warm', 'atom']
words_w_c = []

for word in words:
    if word.startswith(('w', 'c')):
        words_w_c.append(word)

words_final = tuple(words_w_c)
print(words_final)

# read file words.txt and calculate the number 
# of all ascii characters of all words
# open

file_name = 'words.txt'
ascii_chars = 0

with open(file_name, 'r') as f:

    for line in f:
        word = line.rstrip()
        ascii_chars += len(word)

    print(ascii_chars)
```


