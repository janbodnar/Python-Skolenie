# Priklady

## Calculate sum of values

```python
import funcy

data = """
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
"""

lines = data.splitlines()
del lines[0]
print(lines)

# map(str.split, lines)
fields = list(map(lambda line: line.split(','), lines))
print(fields)
fields = list(funcy.flatten(fields))
print(fields)

mysum = sum(map(int, fields))
print(mysum)
```

```python
import funcy

data = """
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
"""

lines = data.splitlines()
del lines[0]
print(lines)

mysum = sum(map(int, funcy.flatten(map(lambda line: line.split(','), lines))))
print(mysum)
```


## map function

```python
def twice(e):
    return 2 * e


vals = [1, -2, 3, 0, 6, -7, 9, 10, -7]

# vals2 = list(map(twice, vals))
vals2 = list(map(lambda e: 2 * e, vals))
print(vals2)
print(vals)
```

## Lambda & filter

```python
words = ['sky', 'auto', 'element', 'pub', 'cup', 'cloud']
words_3_letters = list(filter(lambda word: len(word) == 3, words))

print(words_3_letters)

vals = [1, -2, 3, 0, 6, -7, 9, 10, -7]

negative = list(filter(lambda e: e < 0, vals))
print(negative)
```


## Filter function

```python

def has_3_letters(word):
    if len(word) != 3:
        return True
    else:
        return False


# filter words with three letters
words = ['sky', 'auto', 'element', 'pub', 'cup', 'cloud']
words_3_letters = list(filter(has_3_letters, words))

print(words_3_letters)


def is_negative(e):
    if e < 0:
        return True
    else:
        return False

vals = [1, -2, 3, 0, 6, -7, 9, 10, -7]

negative = list(filter(is_negative, vals))
print(negative)


# negative = []

# for val in vals:
#     if val < 0:
#         negative.append(val)
#
# print(negative)
```



```python
def is_negative(e):
    if e < 0:
        return True
    else:
        return False

vals = [1, -2, 3, 0, 6, -7, 9, 10, -7]

negative = list(filter(is_negative, vals))
print(negative)


# negative = []

# for val in vals:
#     if val < 0:
#         negative.append(val)
#
# print(negative)
```



```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```


## Opakovanie

```python
data = ['falcon', 1, 2, 0, True, 4.5, (1, 2, 3), False, 6.7, 9.0, None]
```













## Generate fake user data

```python
import faker


file_name = 'users.csv'

faker = faker.Faker()


with open(file_name, 'w') as f:

    headers = 'first_name,last_name,job,city,salary\n'
    f.write(headers)

    for _ in range(1000_000):

        fname = faker.first_name()
        lname = faker.last_name()
        job = faker.job()
        city = faker.city()
        salary = faker.random_int(850, 5500, 50)
        
        row = f'{fname},{lname},{job},{city},{salary}\n'

        f.write(row)



# print(fname, lname, job, city)
```

Read CSV data into  list of user objects.

```python
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    job: str
    city: str
    salary: int


file_name = 'users.csv'
all_users = []


with open(file_name, 'r') as f:

    next(f)

    for line in f:
        # print(repr(line))
        row = line.rstrip()
        fields = row.split(';')
    
        user = User(fields[0], fields[1], fields[2], fields[3], int(fields[4]))
        all_users.append(user)

    # print(all_users[:11])


    users_w = [user for user in all_users if user.last_name.startswith('W')]
    print(len(users_w))

    for user in users_w[:21]:
        print(user)
```




## list comprehensions

```python
nums = [1, 2, 3, 4, -5, -6, -7, 8, 9, 10, 10, 10]

negative = [val for val in nums if val < 0]
print(negative)

positive = [val for val in nums if val > 0]
print(positive)
```

```python
from dataclasses import dataclass


@dataclass
class User:
    fname: str
    lname: str
    occupation: str
    age: int


users = [
    User("John", "Doe", "gardener", 56),
    User("Adam", "Roe", "student", 33),
    User("Jane", "Doe", "teacher", 28),
    User("Roger", "Roe", "driver", 67),
    User("Leo", "Abramovic", "singer", 12),
    User("Tomas", "Wager", "programmer", 58),
    User("John", "Adams", "dentist", 33),
    User("Sam", "Brown", "actor", 22),
    User("John", "Smith", "broker", 29),
    User("Rob", "Roe", "dancer", 55),
]

users_w = [user for user in users if user.lname.startswith('W')]
print(users_w)

users_older_40 = [user for user in users if user.age > 40]
print(users_older_40)
```



## Rectangle 

```python
class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


r1 = Rectangle(10, 20)
print(r1.area())

r1.set_width(30)
r1.set_height(40)

print(r1.area())
```


## Dynamic attributes

```python
class Person:
    pass

p = Person()
p.age = 24
p.name = "Peter"
p.occupation = "teacher"

print("{0} is {1} years old an is a {2}".format(p.name, p.age, p.occupation))

p2 = Person()
p2.age = 44
p2.name = "Jozef"
p2.occupation = "programmer"

print("{0} is {1} years old an is a {2}".format(p2.name, p2.age, p2.occupation))
```

## Opakovanie

```python
# create a list of integers only
vals = [1, 2, 3, 4, 5, "12", 4, "21", -1, "3"]

# filter numbers from the list
mixed = [True, False, 1, 0, "True", "False", "1", "0", -1, "1", 11.5, 12, 1.2]

# filter tuples with sum > 10
data = ((3, 4, 2), (3, 3, 4), (4, 4, 4), (3, 3, 3), (1, 1, 1), (1, 2, 3))

# transform the list into lowercased strings
words = ["apple", "Banana", "cherry", "orangE", "KIWI", "maNgo"]

# filter users with age > 40
users = [
    {"first_name": "John", "last_name": "Doe", "age": 30},
    {"first_name": "Jane", "last_name": "Doe", "age": 25},
    {"first_name": "John", "last_name": "Smith", "age": 43},
    {"first_name": "Jane", "last_name": "Smith", "age": 35},
    {"first_name": "John", "last_name": "Doe", "age": 20},
    {"first_name": "Paul", "last_name": "Black", "age": 55},
    {"first_name": "John", "last_name": "Smith", "age": 60},
    {"first_name": "Robert", "last_name": "Smith", "age": 5},
]
```

Riesenie

```python
# transform to a list of integers
vals = [1, 2, 3, 4, 5, "12", 4, "21", -1, "3"]

vals_cleaned = list(map(int, vals))
print(vals_cleaned)


# filter numbers from the list
mixed = [True, False, 1, 0, "True", "False", "1", "0", -1, "1", 11.5, 12, 1.2]

numbers = list(filter(lambda e: type(e) == int or type(e) == float, mixed))
print(numbers)

# filter tuples with sum > 10
data = ((3, 4, 2), (3, 3, 4), (4, 4, 4), (3, 3, 3), (1, 1, 1), (1, 2, 3))

filtered = list(filter(lambda e: sum(e) > 10, data))
print(filtered)

# transform the list into lowercased strings
words = ["apple", "Banana", "cherry", "orangE", "KIWI", "maNgo"]
words_lower = list(map(lambda e: e.lower(), words))
print(words_lower)

# filter users with age > 40
users = [
    {"first_name": "John", "last_name": "Doe", "age": 30},
    {"first_name": "Jane", "last_name": "Doe", "age": 25},
    {"first_name": "John", "last_name": "Smith", "age": 43},
    {"first_name": "Jane", "last_name": "Smith", "age": 35},
    {"first_name": "John", "last_name": "Doe", "age": 20},
    {"first_name": "Paul", "last_name": "Black", "age": 55},
    {"first_name": "John", "last_name": "Smith", "age": 60},
    {"first_name": "Robert", "last_name": "Smith", "age": 5},
]

users_older_40 = list(filter(lambda user: user["age"] > 40, users))
print(users_older_40)
```








## utils module

The `utils.py`:

```python
def filter_len_4(words):
    return list(filter(lambda word: len(word) == 4, words))
    # return filtered
    # return [word for word in words if len(word) == 4]
```

The `main.py`:

```python
import utils

# filter all words having length 4

words = ['cat', 'window', 'word', 'defenestrate', 'cats', 'window', 'cup', 'war', 'rock']

print(utils.filter_len_4(words))
```

Run `python main.py`.  


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


