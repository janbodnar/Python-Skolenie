# Priklady


```python
data = ['atom', -4, 2, True, 'war', -1, 3.4, (), None, 'water', 12, -3]

b = [e for e in data if ... ]
```



## Opakovanie

```python
# print message using fstring: John Doe is 23 years old, he is a gardener
name = "John Doe"
age = 23
occupation = "gardener"

# calculate sum using for loop
# print first, second, last, last but one elements
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print all words starting in 'w'
# sort words
# calculate the sum of all ASCII characters
words = ['small', 'new', 'test', 'sky', 'blue', 'war', 'water']

# print all vowels from the text
text = 'there is an old falcon in the sky'
```

## Riesenia

```python
# print message using fstring: John Doe is 23 years old, he is a gardener
name = "John Doe"
age = 23
occupation = "gardener"

msg = f'{name} is {age} years old, he is a {occupation}'
print(msg)

# calculate sum using for loop
# print first, second, last, last but one elements
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum(vals))

mysum = 0

for val in vals:
    mysum += val

print(mysum)

print(vals[0])
print(vals[1])
print(vals[-1])
print(vals[-2])

# print all words starting in 'w'
# sort words
# calculate the sum of all ASCII characters
words = ['small', 'new', 'test', 'sky', 'blue', 'war', 'water']

for word in words:
    if word.startswith('w'):
        print(word)

words.sort()
print(words)

count_chars = 0

for word in words:
    count_chars += len(word)

print(count_chars)

# print all vowels from the text
# count them
n_of_vowels = 0

text = 'there is an old falcon in the sky'

vowels = {'a', 'e', 'i', 'o', 'u'}

for char in text:
    if char in vowels:
        print(char)
        n_of_vowels += 1

print(n_of_vowels)

```


## cleaning data

```python
words = [' sky ', ' war', '\ncup', 'water', 'ocean', 'warm', 'ten\t', 'cloud', 'wry ']
words_cleaned = []


for word in words:
    words_cleaned.append(word.strip())

print(words)
print(words_cleaned)
```


## startswith

```python
words = ['sky', 'war', 'cup', 'water', 'ocean', 'warm', 'small', 'cloud']

for word in words:
    if word.startswith('w') or word.startswith('c'):
        print(word)

    # if word.startswith(('w', 'c')):
    #     print(word)
```

```python
words = ['sky', 'war', 'cup', 'water', 'ocean', 'warm', 'small', 'cloud', 'wry']

for word in words:
    if word.startswith('w') and len(word) == 3:
        print(word)
```

## calculate sum of CSV data

```python
nums = "1,5,6,8,2,3,1,9"

fields = nums.split(",")
print(fields)

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```


## replace

```python
text = 'an old falcon'

replaced_text = text.replace('a', 'A')

print(replaced_text)
print(text)
```

## String formatting

```python
name = 'Peter'
age = 23
occupation = 'teacher'

# Peter is 23 years old, he is a teacher

print('%s is %d years old, he is a %s' % (name, age, occupation))
print('{} is {} years old, he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old, he is a {occupation}')
```


# len of strings

```python
# Strings with varying character encoding
text1 = "Namaste"  # Regular string
text2 = "नमस्ते"  # Hindi version (Unicode)
text3 = "你好"  # Chinese characters
text4 = "🚀🌍"  # Emojis

# Print lengths to compare
print(len(text1))  # Expected: 7
print(len(text2))  # May not match character count visually!
print(len(text3))  # Length depends on encoding
print(len(text4))  # Emojis may count as multiple characters# Strings with varying character encoding
```



## Two param function

```python
def show_n_times(n, msg):

    for i in range(n):
        print(msg)

show_n_times(3, 'hello there')
show_n_times(10, 'hi!')
```


## function definition

```python
def twice(e):
    return 2 * e

def cube(e):
    return e * e * e

print(twice(10))
print(twice(7))

print(cube(10))
print(cube(22))
```


## print 11

```python
# print 11 
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
print(mix[3][3][3][1])
```


## Filter by type

```python
data = [1, 4.5, True, 1.2, 'falcon', (1, 2, 3), 5, None, 'war', 11]

for e in data:
    if type(e) == float:
        print(e)
```



## type function

```python
x = 1
y = 5.6
z = True
w = 'falcon'
v = (1, 2, 3)

print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(v))
```


## Opakovanie

```python

# print message: Roger Roe is 34 years old, he is a driver and
# lives in Prague
name = "Roger Doe"
age = 34
occupation = 'driver'
city = "Prague"

# print min, max, sum, len of values
# print first, second, last, last but one values

vals = [4, -2, 0, 3, 9, -11, 44, 99, 12, -5]

# print message 6 times
message = 'an old falcon'

# calculate sum of numbers with for or while loop
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

## Riesenie

```python
# print message: Roger Roe is 34 years old, he is a driver and
# lives in Prague
name = "Roger Doe"
age = 34
occupation = 'driver'
city = "Prague"

print(f"{name} is {age} years old, he is a {occupation} and lives in {city}")

# print min, max, sum, len of values
# print first, second, last, last but one values

vals = [4, -2, 0, 3, 9, -11, 44, 99, 12, -5]

print(min(vals))
print(max(vals))
print(sum(vals))
print(len(vals))

print(vals[0])
print(vals[1])
print(vals[-1])
print(vals[-2])


# print message 6 times
message = 'an old falcon'

i = 0

while i < 6:
    print(message)
    i += 1


print(6 * (message + "\n"))
```


## common functions

```python
import statistics

vals = [-2, 0, 3, -1, 9, 11, -8]

print(sum(vals))
print(len(vals))
print(min(vals))
print(max(vals))

print(statistics.mean(vals))
print(statistics.median(vals))
```


## message generation

```python
name = "John Doe"
age = 45
occupation = "gardener"

msg = name + " is " + str(age) + ' years old and he is a ' + occupation
print(msg)
```

```python
name = "John Doe"
age = 45
occupation = "gardener"

# msg = name + " is " + str(age) + ' years old and he is a ' + occupation
# print(msg)

msg = f'{name} is {age} years old and he is a {occupation}'
print(msg)
```


## membership operators

```python
vals = [1, 2, 3, 4, 5]

if 1 in vals:
    print('1 is present')
else:
    print('1 is not present')

if -1 not in vals:
    print('-1 is not present')
else:
    print('-1 is present')
```

## input function

```python
x = input("enter first number: ")
y = input("enter second number: ")

# "5", "3"

print(type(x))
print(type(y))

print(int(x) + int(y))
```


## while cycle

```python
msg = 'an old falcon'
i = 8

while i > 0:
    print(msg)
    i -= 1

print('end of program')
```


## if/elif/else

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('The r variable is negative')
else:
    print('The r variable is zero')

print('end of program')
```





```python
vals = [1, 2, 3, 4, 5]
print(vals)

for val in vals:
    print(val)

words = ['sky', 'book', 'war', 'cup']
print(words)
```



```python
print(r'hello\nthere')


# filename = 'C:/Users/bodnar/Documents/words.txt'
filename = 'data/words.txt'

# C:\Users\bodnar\Documents\pyprogs4\data\words.txt
# C:\Users\bodnar\PycharmProjects\SecondEx\words.txt

with open(filename, 'r') as fd:

    for line in fd:
        print(line.strip())


print('finished ')
```


```python
filename = 'data/words.txt'
with open(filename, 'r') as fd:

    lines = fd.readlines()
    print(lines)

    words = list(map(lambda word: word.strip(), lines))
    words.pop()
    print(words)

    for word in words:
        print(word, end=' ')

print()
print('finished ')
```


## calculate sum

```python
# calculate sum
data = '1,2,3,4,5,6,7,8,9,10'

print(sum(map(int, data.split(','))))

vals = list(map(int, data.split(',')))
print(vals)
```


## map function

```python
# def toabs(e):
#     if e < 0:
#         return -e
#     else:
#         return e

vals = [1, 2, 3, -4, 5, -6, 7, -8, 9, 10]

# vals_abs = list(map(lambda e: abs(e) , vals))
vals_abs = list(map(abs , vals))
print(vals_abs)
```


```python
def twice(e):
    return 2 * e


vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

vals_2x = list(map(lambda e: 2 * e , vals))
print(vals_2x)

vals_2x = list(map(twice , vals))
print(vals_2x)

print(vals)
```




## lambda functions

```python
words = ['sky', 'blue', 'war', 'cup', 'atom', 'forest', 'new', 'water', 'top']

words_w = list(filter(lambda word: word.startswith('w') , words))
print(words_w)

words_w = list(filter(lambda word: word[0] == 'w' , words))
print(words_w)
```



```python
vals = [1, 2, -3, 4, 5, 6, -5, -2]

negatives = list(filter(lambda e: e < 0 , vals))
print(negatives)


evens = list(filter(lambda e: e % 2 == 0, vals))
print(evens)
```

```python
def has_three_chars(word):
    if len(word) == 3:
        return True
    else:
        return False


words = ['sky', 'blue', 'cup', 'atom', 'forest', 'new', 'top']


words_3c = list(filter(lambda word: len(word) == 3 , words))
print(words_3c)

words_3c = list(filter(has_three_chars, words))
print(words_3c)
```


## filter

```python
def is_negative(e):
    if e < 0:
        return True
    else:
        return False

vals = [1, 2, -3, 4, 5, 6, -5, -2]

negatives = list(filter(is_negative, vals))
print(negatives)

# negatives = []

# for val in vals:
#     if val < 0:
#         negatives.append(val)

# print(negatives)
```





```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```



## numpy

```python
import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Multiply each element by 3
result = array * 3

print("Original array:", array)
print("Array after multiplication:", result)
```



## type function

```python
items = ("oranges", 1, 2, True, "apples", False, "bananas", 2.3, (1, 2))

print(items)

for item in items:

   if type(item) == str:
      print(item)
```


## Opakovanie

```python

# print output using fstring: John Doe is 34 years old and he is a gardener
name = 'John Doe'
age = 34
occupation = 'gardener'


# compute sum using for loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In the text, replace all 'r' with 'R'
text = 'There are many stars in the night sky.'

# calculate the number of vowels in the text
text2 = 'and old falcon in the sky'
```

## Riesenia

```python

# print output using fstring: John Doe is 34 years old and he is a gardener
name = 'John Doe'
age = 34
occupation = 'gardener'

msg = f'{name} is {age} years old and he is a {occupation}'
print(msg)


# compute sum using for loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0

for val in vals:
   mysum += val

print(mysum)

# In the text, replace all 'r' with 'R'
text = 'There are many stars in the night sky.'

text_modified = text.replace('r', 'R')
print(text_modified)


# calculate the number of vowels in the text

n_vowels = 0
vowels = 'aeiouy'

text2 = 'and old falcon in the sky'

for character in text2:
   if character in vowels:
      n_vowels += 1

print(n_vowels)
`

## Splitting


```python
nums = "1,5,6,8,2,3,1,9"

fields = nums.split(",")
print(fields)

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```


```python
name = "John Doe"
age = 34
occupation = "gardener"

print(f'{name} is {age} years old and he is a {occupation}')
```

















## Excel sheets

```python
import openpyxl

book = openpyxl.load_workbook('sheets.xlsx')

print(book.sheetnames)

sheet1 = book["January"]
sheet1['A1'] = 22

sheet2 = book["March"]
print(sheet2.title)

sheet2['B4'] = 11

book.save('sheets2.xlsx')
```




```python
import re

data = "1,2;3,4;5,6;7,8;9,10"

vals = re.split(r'[,;]', data)
print(vals)

print(sum(map(int, vals)))
```

## Opakovanie

The `mumbers.csv` file:

```
1,2,3,4,5,6,7,8,9,10
11,12,13,14,15,16,17,18,19,20
```


The `users.csv` file:

```
id,first_name,last_name,occupation,salary
1,John,Doe,gardener,1200
2,Roger,Roe,driver,2300
3,Jane,Smith,teacher,2500
4,Emily,Jones,nurse,2700
5,Michael,Brown,chef,2200
6,Jessica,Davis,engineer,3000
7,David,Wilson,artist,1800
8,Laura,Moore,scientist,3200
9,James,Taylor,writer,2100
10,Anna,Anderson,lawyer,3500
11,Robert,Thomas,doctor,4000
12,Patricia,Jackson,architect,3300
13,Charles,White,mechanic,2400
14,Barbara,Harris,pharmacist,2900
15,Daniel,Martin,accountant,2800
16,Elizabeth,Thompson,designer,2600
17,Matthew,Garcia,plumber,2300
18,Susan,Martinez,manager,3100
19,Christopher,Robinson,lawyer,3400
20,Mary,Clark,analyst,3700
21,Anthony,Rodriguez,consultant,3600
22,Linda,Lewis,therapist,3800
23,Mark,Lee,technician,2500
24,Jennifer,Walker,lawyer,3000
25,Paul,Hall,teacher,2700
```



```python
# filter words starting with 'w', case insensitive
# transform into a list of words with lowercase letters
words = ['sky', 'Water', 'warm', 'OLD', 'small', 'war', 'forest', 'WRONG']

# from numbers.csv file, calculate sum, len, min, max

# read users.csv and filter all doctors and lawyers
# extract the salaries column and calculate sum, min, max

# read users from https://webcode.me/users.json and filter out those 
# with last name starting with 'B'

# generate CSV file having 10_000 lines of random values, 10 per line
```


## Riesenia

```python
# filter words starting with 'w', case insensitive
# transform into a list of words with lowercase letters
words = ['sky', 'Water', 'warm', 'OLD', 'small', 'war', 'forest', 'WRONG']

words_w = [word for word in words if word.startswith(('w', 'W'))]
print(words_w)

words_lowercase = [word.lower() for word in words]
print(words_lowercase)



import csv

filename = 'numbers.csv'
vals = []

with open(filename, 'r') as fd:

    reader = csv.reader(fd)

    for line in reader:
        line_ints = [int(e) for e in line]
        vals.extend(line_ints)

print(vals)
print(len(vals))
print(min(vals))
print(max(vals))
print(sum(vals))



import csv

filename = "users.csv"
users = []

with open(filename, "r") as fd:

    reader = csv.DictReader(fd)

    for line in reader:
        users.append(line)

# print(users)

users_doctors_lawyers = [
    user for user in users if user["occupation"] in ("doctor", "lawyer")
]

print(users_doctors_lawyers)

salaries = [int(user['salary']) for user in users]
print(salaries)
print(min(salaries))
print(max(salaries))
print(sum(salaries))
print(len(salaries))



import requests

url = 'https://webcode.me/users.json'
resp = requests.get(url)

data = resp.json()
users = data['users']

users_b = [user for user in users if user['last_name'][0] == 'B']
print(users_b)



import random

filename = 'rand_vals.csv'

with open(filename, 'w') as fd:

    for idx in range(10_000):
        rand_line = []

        for idx2 in range(10):
            r = random.randint(0, 100)
            rand_line.append(r)

        rand_line_s = [str(e) for e in rand_line]
        row = ','.join(rand_line_s) + "\n"
        
        fd.write(row)
```











## filter file types

```python
import os 

files = os.listdir('.')
# print(files)

pyfiles = [file for file in files if file.endswith('py')]
print(pyfiles)

csv_files = [file for file in files if file.endswith('csv')]
print(csv_files)
```



## file paths

```python
import os 

# oldname = 'C:\\Users\\bodnar\\Documents\\pyprogs2\\words2.txt'
# newname = 'C:\\Users\\bodnar\\Documents\\pyprogs2\\words.txt'

# oldname = 'C:/Users/bodnar/Documents/pyprogs2/words2.txt'
# newname = 'C:/Users/bodnar/Documents/pyprogs2/words.txt'

oldname = r'C:\Users\bodnar\Documents\pyprogs2\words.txt'
newname = r'C:\Users\bodnar\Documents\pyprogs2\words2.txt'

os.rename(oldname, newname)
```


## generate data with related emails

```python
from faker import Faker
import random

faker = Faker()
filename = "users.csv"

email_domains = (
    "example.com",
    "gmail.com",
    "hotmail.com",
    "simplemail.com",
    "yahoo.com",
)


with open(filename, "w") as fd:

    fd.write("id,first_name,last_name,email,salary\n")

    for idx in range(1, 10_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = f'{first_name}.{last_name}@{random.choice(email_domains)}'
        salary = faker.random_int(1200, 5000)

        line = f"{idx},{first_name},{last_name},{email},{salary}\n"

        fd.write(line)

print('program finished')
```



## read users

```python

import csv


filename = 'users.csv'
users = []


with open(filename, 'r') as fd:

    reader = csv.DictReader(fd)

    for row in reader:
        users.append(row)

# print(users[:11])
# print(users[-11:])

users_salary_gt_4500 = [user for user in users if int(user['salary']) > 4500]
print(len(users_salary_gt_4500))

users_last_name_w = [user for user in users if user['last_name'].startswith('W')]
print(len(users_last_name_w))
```



## generate fake users

```python
from faker import Faker

faker = Faker()
filename = "users.csv"

with open(filename, "w") as fd:

    fd.write("id,first_name,last_name,email,salary\n")

    for idx in range(1, 10_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        salary = faker.random_int(1200, 5000)

        line = f"{idx},{first_name},{last_name},{email},{salary}\n"

        fd.write(line)

print('program finished')
```



## Dictionary reader

```python
import csv

vals = []

filename = "users.csv"
with open(filename, "r") as f:

    reader = csv.DictReader(f)

    for row in reader:

        print(row['first_name'], row['last_name'], row['salary'])
        vals.append(row)


print(vals)
```


## csv module

```python
import csv

vals = []

filename = "numbers.csv"
with open(filename, "r") as f:

    reader = csv.reader(f)

    # print(list(reader))

    for row in reader:

        for e in row:
            vals.append(int(e))


print(vals)
```



## List comprehensions

```python
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


evens = [val for val in vals if val % 2 == 0]
print(evens)

odds = [val for val in vals if val % 2 == 1]
print(odds)

# evens = list(filter(lambda e: e % 2 == 0, vals))
# print(evens)

# odds = list(filter(lambda e: e % 2 == 1, vals))
# print(odds)
```

```python
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ['sky', 'war', 'water', 'small', 'wow', 'cup', 'cloud']

words_w = [word for word in words if word.startswith('w')]
print(words_w)

# words_w_c = [word for word in words if word.startswith('w') or word.startswith('c')]
words_w_c = [word for word in words if word.startswith(('w', 'c'))]
print(words_w_c)
```

```python
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

words = ['SKY', 'war', 'water', 'SMALL', 'wow', 'Cup', 'cloud']

words_small = [word.lower() for word in words] 
print(words_small)
print(words)
```

```python
vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

vals2 = [int(val) for val in vals]
print(vals2)
```








```
The Battle of Thermopylae was fought between an alliance of Greek city-states, 
led by King Leonidas of Sparta, and the Persian Empire of Xerxes I over the 
course of three days, during the second Persian invasion of Greece.
```


## Opakovanie

```python
# calculate sum
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# calculate sum
data = [1, True, 2, 'hello', 3, 4, 5, 'water', 6, 7, 8, 9, 10]

# create flattened tuple
data = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10))

# generate a tuple of random 20 value between 1 .. 100
# randomly pick a value from the tuple
# randomly pick three values from the tuple


# The Battle of Thermopylae was fought between an alliance of Greek city-states, 
# led by King Leonidas of Sparta, and the Persian Empire of Xerxes I over the 
# course of three days, during the second Persian invasion of Greece.

# read file
# count the number of words
# count the number of unique words

# clean the message from these chars: ?,~.
msg = 'there ?are !three falcons. in the sky,'

# filter words that contain 'r'
words = ['word', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana', 
         'small', 'terrific', 'alternative', 'book', 'dictionary', 'word']
```


## Riesenia

```python
# calculate sum
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

data2 = []

for val in data:
    data2.append(int(val))

print(data2)
print(sum(data2))

print(sum(map(int, data)))


data = [1, True, 2, 'hello', 3, 4, 5, 'water', 6, 7, 8, 9, 10]

data2 = list(filter(lambda e: type(e) == int, data))
print(data2)
print(sum(data2))

def is_int(e):
    if type(e) == int:
        return True
    else:
        return False


# calculate sum
data = [1, True, 2, 'hello', 3, 4, 5, 'water', 6, 7, 8, 9, 10]

data2 = list(filter(lambda e: type(e) == int, data))
# data2 = list(filter(is_int, data))
print(data2)
print(sum(data2))

import funcy

# create flattened tuple
data = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10))
data2 = []

# data2.extend(data)
# print(data2)

for val in data:
    if type(val) == int:
        data2.append(val)
    elif type(val) == tuple:
        data2.extend(val)


data3 = tuple(data2)
print(data3)


data3 = tuple(funcy.flatten(data))
print(data3)


import random

rand_data = []

for i in range(20):
    r = random.randint(1, 100)
    rand_data.append(r)


rand_data2 = tuple(rand_data)
print(rand_data2)

print(random.choice(rand_data2))
print(random.choices(rand_data2, k=3))


import re

# clean the message from these chars: ?,~.
msg = 'there ?are !three falcons. in the sky,'

cleaned = msg.replace('?', '').replace('!', '').replace('.', '').replace(',', '')
print(cleaned)

cleaned2 = re.sub(r'[,.!?]', '', msg)
print(cleaned2)


# msg2 = msg.replace('?', '')
# print(msg2)

# msg3 = msg2.replace('!', '')
# print(msg3)

# msg4 = msg3.replace('.', '')
# print(msg4)

# msg5 = msg4.replace(',', '')
# print(msg5)



import funcy

filename = 'thermopylae.txt'

with open(filename, 'r') as fd:

    content = fd.read()
    cleaned = content.replace(',', '').replace('.', '')
    words = cleaned.split()
    print(words)

    print(len(words))
    print(len(set(words)))
    print(len(list(funcy.distinct(words))))


# filter words that contain 'r'
words = [
    "word",
    "sky",
    "tomorrow",
    "cat",
    "dog",
    "apple",
    "orange",
    "banana",
    "small",
    "terrific",
    "alternative",
    "book",
    "dictionary",
    "word",
]


words2 = list(filter(lambda word: "r" in word, words))
print(words2)


```


```sql
CREATE TABLE users(id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), salary INT);
```


```python
from faker import Faker

faker = Faker()

filename = "users.csv"
with open(filename, "w") as file:

    for idx in range(1, 1000_001):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        salary = faker.random_int(min=1000, max=10_000, step=100)

        row = f"{idx},{first_name},{last_name},{email},{salary}\n"

        file.write(row)

        if idx % 100_000 == 0:
            print(f"Processed {idx} rows")

print(f"Finished writing {filename} with {idx} rows")
```


```sql
CREATE TABLE cars2(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT);
```


## Fetch cars from database

```python
import psycopg
from collections import namedtuple

Car = namedtuple('Car', ['id', 'name', 'price'])

cs = "dbname='testdb' user='postgres' password='postgres'"
cars = []

with psycopg.connect(cs) as con:
        
        with con.cursor() as cur:
    
            cur.execute("SELECT id, name, price FROM cars")
            rows = cur.fetchall()

            # print(rows)

            for row in rows:
                # car = Car(*row)
                car = Car(id=row[0], name=row[1], price=row[2])
                cars.append(car)


# print(cars)

filtered_cars = [car for car in cars if car.price < 30_000]
# print(filtered_cars)

for car in filtered_cars:
     print(car)
```





```python
# calculate min/max and mean of salaries
users = [
    {"first_name": "John", "last_name": "Doe", "salary": 2300},
    {"first_name": "Roger", "last_name": "Roe", "salary": 1800},
    {"first_name": "Paul", "last_name": "Smith", "salary": 2100},
    {"first_name": "Roman", "last_name": "Novak", "salary": 800},
    {"first_name": "Lucia", "last_name": "Black", "salary": 3200},
]
```




## Read web page

```python
import requests

url = 'https://webcode.me'

resp = requests.get(url)
content = resp.text

# print(content)

filename = 'webcode_home.html'

with open(filename, 'w') as fd:

    fd.write(content)
```


## Generate fake data

```python
from faker import Faker

faker = Faker()

filename = 'users.csv'

with open(filename, 'w') as fd:

    for idx in range(1, 100_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()

        fd.write(f"{idx},{first_name},{last_name},{email},{city}\n")
```



## User objects from a CSV file

```csv
First Name,Last Name,Email
John,Doe,john.doe@example.com
Jane,Smith,jane.smith@example.com
Alice,Brown,alice.brown@example.com
Bob,Johnson,bob.johnson@example.com
Emily,Davis,emily.davis@example.com
Michael,Williams,michael.williams@example.com
Sarah,Miller,sarah.miller@example.com
David,Wilson,david.wilson@example.com
Laura,Anderson,laura.anderson@example.com
Chris,Moore,chris.moore@example.com
Jessica,Taylor,jessica.taylor@example.com
Daniel,Thomas,daniel.thomas@example.com
Sophia,Jackson,sophia.jackson@example.com
Ethan,White,ethan.white@example.com
Emma,Harris,emma.harris@example.com
Matthew,Martin,matthew.martin@example.com
Olivia,Thompson,olivia.thompson@example.com
James,Garcia,james.garcia@example.com
Liam,Martinez,liam.martinez@example.com
Isabella,Robinson,isabella.robinson@example.com
```


```python
from dataclasses import dataclass
import csv

@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    email: str

# Read users from the CSV file and create User objects
def read_users_from_csv(file_name):
    users = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(
                first_name=row["First Name"],
                last_name=row["Last Name"],
                email=row["Email"]
            )
            users.append(user)
    return users

# Example usage
file_name = "users.csv"  # Replace with your CSV file name
user_list = read_users_from_csv(file_name)

# Print the list of User objects
for user in user_list:
    print(user)
```






## Rectangle class

```python
class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def set_width(self, width):

        self.width = width

    def get_width(self):

        return self.width

    def set_height(self, height):

        self.height = height

    def height(self):

        return self.height


r = Rectangle(10, 10)
print(r.area())

r.set_height(20)
r.set_width(30)

print(r.area())
```




## The __str__ method

```python
class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):
        return f'Cat: Name {self.name}, Age {self.age}'

missy = Cat('Missy', 5)
lucky = Cat('Lucky', 8)

print(missy)
print(lucky)

print(missy.name, missy.age)
print(lucky.name, lucky.age)
```



## id of objects

```python
class Being:

    def __init__(self):
        print("Being is initialized")

b1 = Being()
print(id(b1))

b2 = Being()
print(id(b2))
```



## funcy library

Functional programming

```python
import funcy

# create flattened tuple  (1, 2, 3, 4, 5, 6, 7, 8, 9)
vals2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

flattened = tuple(funcy.flatten(vals2))
print(flattened)

# unique values
data = (1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7)
uniques = tuple(funcy.distinct(data))
print(uniques)


# divide into positive & negative
vals = [1, -2, 2, -3, 4, 5, -6]
positive, negative = funcy.split(lambda x: x > 0, vals)

print(list(positive))
print(list(negative))
```



## Opakovanie

The `words.txt` file:

```
sky
wOrd
waR
TOWN
AuTo
```


```python
# filter odd numbers
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter out words containing k or w
words = ['sky', 'pen', 'know', 'town', 'own', 'kit', 'clown']

# calculate sum, len, max, min from numbers
data = '1;2;3;4;5;6;7;8;9;10'

# clean data
data2 = ["row\n", "  small", "own  ", "tomorrow\t\t", " basic "]

# create flattened tuple  (1, 2, 3, 4, 5, 6, 7, 8, 9)
vals2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# from the words.txt file creat list ["auto", "sky", "town", "war", "word"]
```

## Riesenia

```python
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_vals = list(filter(lambda val: val % 2 == 1, vals))
print(odd_vals)

words = ["sky", "pen", "know", "town", "own", "kit", "clown"]

words_k_w = list(filter(lambda word: "k" in word or "w" in word, words))
print(words_k_w)

# calculate sum, len, max, min from numbers
data = '1;2;3;4;5;6;7;8;9;10'
 
vals = list(map(int, data.split(';')))
print(vals)
print(sum(vals))
print(len(vals))
print(min(vals))
print(max(vals))

data2 = ["row\n", "  small", "own  ", "tomorrow\t\t", " basic "]

cleaned_data = list(map(lambda e: e.strip(), data2))
print(cleaned_data)

# create flattened tuple  (1, 2, 3, 4, 5, 6, 7, 8, 9)

flattened = []

vals2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for nested in vals2:
    flattened.append(nested)

print(flattened)

vals3 = tuple(flattened)
print(vals3)


# from the words.txt file creat list ["auto", "sky", "town", "war", "word"]

filename = 'words.txt'

words = []

with open(filename, 'r') as fd:

    for line in fd:
        words.append(line.strip().lower())
        
    words.sort()
    print(words)
```



## importing modules

```python
#!/usr/bin/python

# import math

# print(math.pi.__doc__)
# print(math.cos.__doc__)
# print(math.sin.__doc__)
# print(math.log.__doc__)
# print(math.floor.__doc__)
# print(math.exp.__doc__)

from math import pi, cos, sin, log, floor, exp

print(pi.__doc__)
print(cos.__doc__)
print(sin.__doc__)
print(log.__doc__)
print(floor.__doc__)
print(exp.__doc__)
```



## Read CSV file

```python

import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv', header=None)

print(df)

# Calculate the total sum using df.values.sum()
total_sum = df.values.sum()

print("Sum of all values:", total_sum)



# filename = 'data.csv'
#
# vals = []
#
# with open(filename, 'r') as fd:
#
#     for line in fd:
#         fields = line.strip().split(',')
#         # print(fields)
#         nums = list(map(int, fields))
#         vals.extend(nums)
#
#     print(vals)
#     print(len(vals))
#     print(sum(vals))
#     print(max(vals))
```


## write function

```python
filename = 'words2.txt'
with open(filename, 'a') as fd:

    fd.write('war\n')
    fd.write('water\n')
    fd.write('warm\n')
```

## writelines function

```python
filename = 'words2.txt'

words = ['new\n', 'red\n', 'brown\n']

with open(filename, 'a') as fd:

    fd.writelines(words)
```


## read line by line

```python
lines = []

filename = 'words.txt'
with open(filename, 'r') as fd:

    for line in fd:
        lines.append(line.strip())

print(lines)
```


## read words

```python
filename = 'words.txt'
with open(filename, 'r') as fd:

    lines = fd.readlines()
    print(lines)

    cleaned_lines = list(map(lambda line: line.strip(), lines))
    print(cleaned_lines)

    for line in cleaned_lines:
        print(line)
```



## split/map

```python
data = "1,2,3,4,5,6,7,8,9,10"

fields = data.split(',')
print(fields)

vals2 = list(map(int, fields))
print(vals2)
print(sum(vals2))
print(len(vals2))
print(max(vals2))
```




## Map function


```python
vals = [1, 2, 3, 4, 5, 6]
print(vals)

def twice(val):
    return 2 * val

def cube(val):
    return val * val * val


# result = list(map(cube, vals))
result = list(map(lambda val: val ** 3, vals))

print(vals)
print(result)
```


abs function

```python
vals = [1, 2, -3, -4, 5, -6]
print(vals)


result = list(map(lambda val: abs(val), vals))

print(vals)
print(result)
```



## filter

filter funkcia

```python
# positives
vals = [-2, 2, 0, 1, 9, 8, -7, 3]

def is_pos(val):
    if val > 0:
        return True
    else:
        return False

# vals_pos = list(filter(is_pos, vals))
vals_pos = list(filter(lambda e: e > 0, vals))
print(vals_pos)

# negatives

def is_neg(val):
    if val < 0:
        return True
    else:
        return False

# vals_neg = list(filter(is_neg, vals))
vals_neg = list(filter(lambda e: e < 0, vals))
print(vals_neg)
```

Filtering words

```python
words = ['small', 'true', 'sky', 'bye', 'raw', 'ten', 'forest', 'cloud', 'war']


def has_3_chars(word):
    if len(word) == 3:
        return True
    else:
        return False

# len/filter

# words_3 = list(filter(has_3_chars, words))
words_3 = list(filter(lambda word: len(word) == 3, words))
print(words_3)
```

```python
words = ['small', 'true', 'sky', 'bye', 'raw', 'ten', 'forest', 'cloud', 'war']
# starting w or c

def starts_w_c(word):
    if word.startswith(('w', 'c')):
        return True
    else:
        return False

# words_3 = list(filter(starts_w_c, words))
words_3 = list(filter(lambda word: word.startswith(('w', 'c')), words))
print(words_3)
```






## Opakovanie


```
sky
blue
supper
new
bod
raw
forest
falcon
```



```python
# print message: John Doe is 34 years old and he is a gardener
name = "John Doe"
age = 34
occupation = 'gardener'

# calculate sum using for/while loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# calculate minimum, maximum, number of els, sum, mean
# use functions
vals2 = [1, -2, 13, 24, 5, 9]

# transform this list to a list of positive values
vals3 = [2, -3, -1, 0, 2, 3, 9, 3, -9]

# filter out all words ending in 'l'
words = ['sky', 'war', 'portal', 'earth', 'small']

# filter all words that have r character
words2 = ['spy', 'rust', 'tomorrow', 'water', 'war', 'cup']


# read the words.txt file and print all words in uppercase
```


## Riesenia

```python
name = "John Doe"
age = 34
occupation = 'gardener'

print(f'{name} is {age} years old and he is a {occupation}')

# calculate sum using for/while loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0

for val in vals:
    mysum += val

print('the sum of values is:', mysum)

import statistics

# calculate minimum, maximum, number of elements, sum, mean
# use functions
vals2 = [1, -2, 13, 24, 5, 9]

print(min(vals2))
print(max(vals2))
print(len(vals2))
print(sum(vals2))

print(sum(vals2)/len(vals2))
print(statistics.mean(vals2))


vals3 = [2, -3, -1, 0, 2, 3, 9, 3, -9]

vals_pos = []

for val in vals3:
    vals_pos.append(abs(val))

print(vals_pos)


# filter out all words ending in 'l'
words = ['sky', 'war', 'portal', 'earth', 'small']
words_l = []

for word in words:
    if word.endswith('l'):
        words_l.append(word)

print(words_l)

# ---------------------------------------------

def ends_in_l(e):
    if e.endswith('l'):
        return True
    else:
        return False

# words_l2 = list(filter(ends_in_l, words))
words_l2 = list(filter(lambda word: word.endswith('l'), words))
print(words_l2)


# filter all words that have r character
words2 = ['spy', 'rust', 'tomorrow', 'water', 'war', 'cup']

words2_r = []

for word in words2:
    if 'r' in word:
        words2_r.append(word)

print(words2_r)

```








## Real all p tags from sme.sk

```python
from selectolax.parser import HTMLParser
import requests

url = 'https://sme.sk'

resp = requests.get(url)
html = resp.text

tree = HTMLParser(html)

p_tags = tree.css('p')

for p in p_tags:
    print(p.text())
```




## Read all li tags

```python
from selectolax.parser import HTMLParser

with open('index.html', 'r') as f:

    html = f.read()

    tree = HTMLParser(html)
    li_tags = tree.css('li')

    for li in li_tags:
        print(li.text())
```



## Read hydro data

```python
import pandas as pd

url = 'https://www.shmu.sk/sk/?page=1&id=ran_sprav'
tables = pd.read_html(url)
df = tables[0]

print(df)
```



## Opakovanie


```python
# read HTML data from https://webcode.me

# print all directories from PATH environment variable, (os.environ.get)


# calculate min, max, sum, avg of user salaries

import sqlite3

# Using with statement for automatic connection management
with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    
    # Single executescript with all statements and data
    cursor.executescript('''
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            salary REAL NOT NULL
        );
        
        INSERT INTO users (id, first_name, last_name, email, salary) VALUES
            (1, 'John', 'Smith', 'john.smith@example.com', 55000.00),
            (2, 'Emma', 'Johnson', 'emma.johnson@example.com', 62000.00),
            (3, 'Michael', 'Williams', 'michael.williams@example.com', 48000.00),
            (4, 'Sophie', 'Brown', 'sophie.brown@example.com', 75000.00),
            (5, 'William', 'Jones', 'william.jones@example.com', 68000.00),
            (6, 'Olivia', 'Garcia', 'olivia.garcia@example.com', 52000.00),
            (7, 'James', 'Miller', 'james.miller@example.com', 89000.00),
            (8, 'Ava', 'Davis', 'ava.davis@example.com', 47000.00),
            (9, 'Alexander', 'Rodriguez', 'alexander.rodriguez@example.com', 65000.00),
            (10, 'Isabella', 'Martinez', 'isabella.martinez@example.com', 71000.00),
            (11, 'Daniel', 'Hernandez', 'daniel.hernandez@example.com', 58000.00),
            (12, 'Mia', 'Lopez', 'mia.lopez@example.com', 63000.00),
            (13, 'Thomas', 'Gonzalez', 'thomas.gonzalez@example.com', 79000.00),
            (14, 'Charlotte', 'Wilson', 'charlotte.wilson@example.com', 54000.00),
            (15, 'David', 'Anderson', 'david.anderson@example.com', 86000.00),
            (16, 'Amelia', 'Thomas', 'amelia.thomas@example.com', 61000.00),
            (17, 'Joseph', 'Taylor', 'joseph.taylor@example.com', 72000.00),
            (18, 'Emily', 'Moore', 'emily.moore@example.com', 67000.00),
            (19, 'Robert', 'Jackson', 'robert.jackson@example.com', 93000.00),
            (20, 'Grace', 'Martin', 'grace.martin@example.com', 59000.00);
    ''')

# calculate min, max, sum, avg for CSV data

import csv

# Write to CSV file
with open('users_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(['id', 'first_name', 'last_name', 'email', 'salary'])
    
    # Write 20 specific users
    writer.writerows([
        [1, 'John', 'Smith', 'john.smith@example.com', 55000.00],
        [2, 'Emma', 'Johnson', 'emma.johnson@example.com', 62000.00],
        [3, 'Michael', 'Williams', 'michael.williams@example.com', 48000.00],
        [4, 'Sophie', 'Brown', 'sophie.brown@example.com', 75000.00],
        [5, 'William', 'Jones', 'william.jones@example.com', 68000.00],
        [6, 'Olivia', 'Garcia', 'olivia.garcia@example.com', 52000.00],
        [7, 'James', 'Miller', 'james.miller@example.com', 89000.00],
        [8, 'Ava', 'Davis', 'ava.davis@example.com', 47000.00],
        [9, 'Alexander', 'Rodriguez', 'alexander.rodriguez@example.com', 65000.00],
        [10, 'Isabella', 'Martinez', 'isabella.martinez@example.com', 71000.00],
        [11, 'Daniel', 'Hernandez', 'daniel.hernandez@example.com', 58000.00],
        [12, 'Mia', 'Lopez', 'mia.lopez@example.com', 63000.00],
        [13, 'Thomas', 'Gonzalez', 'thomas.gonzalez@example.com', 79000.00],
        [14, 'Charlotte', 'Wilson', 'charlotte.wilson@example.com', 54000.00],
        [15, 'David', 'Anderson', 'david.anderson@example.com', 86000.00],
        [16, 'Amelia', 'Thomas', 'amelia.thomas@example.com', 61000.00],
        [17, 'Joseph', 'Taylor', 'joseph.taylor@example.com', 72000.00],
        [18, 'Emily', 'Moore', 'emily.moore@example.com', 67000.00],
        [19, 'Robert', 'Jackson', 'robert.jackson@example.com', 93000.00],
        [20, 'Grace', 'Martin', 'grace.martin@example.com', 59000.00]
    ])
```

## Riesenia

```python
import requests

url = "https://webcode.me"

resp = requests.get(url)
print(resp.text)

# ----------------------------

import os

text = os.environ.get("PATH")
print(text)

folders = text.split(';')
for folder in folders:
    print(folder)

# ----------------------------

import sqlite3
import statistics

salaries = []

with sqlite3.connect('test.db') as con:

    cur = con.cursor()

    sql = 'SELECT salary from users'
    cur.execute(sql)

    for row in cur:
        salaries.append(row[0])

print(min(salaries), max(salaries), sum(salaries), statistics.mean(salaries))

# -----------------------------

import csv 
import statistics

filename = 'users_2.csv'
salaries = []

with open(filename, 'r') as fd:

    reader = csv.DictReader(fd)

    for row in reader:
        salaries.append(round(float(row['salary'])))

print(min(salaries), max(salaries), sum(salaries), statistics.mean(salaries))

```

```sql
SELECT MIN(salary), MAX(salary), SUM(salary), AVG(salary) FROM users;
```



## Read CSV with different number of rows in Pandas

```python
import pandas as pd

# Read the file with flexible parsing
df = pd.read_csv('numbers.csv', 
                 sep='[;,]', 
                 engine='python',  # Python engine is more flexible
                 names=['c1','c2','c3','c4','c5','c6','c7'],  # Explicitly set column names
                 header=0)  # Use first row as header

# Fill missing values with NaN or another value if needed
df = df.fillna(0)  # or df.fillna(0) for zeros

print(df)
```


## compare two files

```python
import filecmp

# Paths to the files
file1 = 'words1.txt'
file2 = 'words2.txt'

# Compare the files
are_files_equal = filecmp.cmp(file1, file2, shallow=False)

if are_files_equal:
    print("The files are identical.")
else:
    print("The files are different.")
```


```python
import pandas as pd

# pip install pandas lxml

# URL of the JSON data
url = 'https://webcode.me/users.json'

# Read the JSON data into a DataFrame
df = pd.read_json(url)

# Export the DataFrame directly to an XML file
df.to_xml("users.xml", root_name="users", row_name="user")

print("XML data has been written directly to 'users.xml'.")
```



## Read JSON into XML

```python
import requests
import xml.etree.ElementTree as ET

# URL of the JSON data
url = 'https://webcode.me/users.json'

# Fetch JSON data from the URL
response = requests.get(url)
data = response.json()

# Create the root XML element
root = ET.Element("users")

# Iterate through the users and populate the XML tree
for user in data['users']:
    user_element = ET.SubElement(root, "user")
    ET.SubElement(user_element, "id").text = str(user["id"])
    ET.SubElement(user_element, "first_name").text = user["first_name"]
    ET.SubElement(user_element, "last_name").text = user["last_name"]
    ET.SubElement(user_element, "email").text = user["email"]

# Convert the XML tree to a string
xml_data = ET.tostring(root, encoding='utf-8', method='xml').decode()

# Save the XML data to a file (optional)
with open("users.xml", "w") as xml_file:
    xml_file.write(xml_data)

print("XML data:")
print(xml_data)
```





## Dump users to file

```python
import json

# Create a list of 20 users
data = [
    {"name": "Jane", "age": 17},
    {"name": "John", "age": 22},
    {"name": "Alice", "age": 19},
    {"name": "Bob", "age": 25},
    {"name": "Mary", "age": 20},
    {"name": "Tom", "age": 18},
    {"name": "Lucy", "age": 23},
    {"name": "Mark", "age": 21},
    {"name": "Nina", "age": 24},
    {"name": "James", "age": 26},
    {"name": "Linda", "age": 19},
    {"name": "David", "age": 22},
    {"name": "Sophia", "age": 27},
    {"name": "Chris", "age": 20},
    {"name": "Emma", "age": 23},
    {"name": "Andrew", "age": 21},
    {"name": "Olivia", "age": 28},
    {"name": "Peter", "age": 18},
    {"name": "Chloe", "age": 24},
    {"name": "Tommy", "age": 25}
]

fname = 'friends.json'

# Write the list of users to a JSON file
with open(fname, 'w') as f:
    json.dump(data, f, indent='    ')

print(f'{len(data)} users have been written to {fname}.')
```



## Sum script arguments

```python
import sys

data = sys.argv[1:]

suma = sum(map(int, data))
print(suma)
```



## Opakovanie

The `words.txt` file:

```
war
Water
small
NICE
rock
final
loW
```


```python
# print all vowels
text = 'there are many stars in the sky'

# remove punctunation characters (?!.) from the text
text2 = 'And old falcon? Yes! Stars in the sky.'


# pick 3 numbers randomly and calculate sum
# sort values in asc/desc orders
numbers = [2, 3, 1, 6, 7, 8, 3, 4, 9, 2, 9]


# create nums2 that contains unique values
nums = [2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 9]

# calculate sum
# transform into (1, 2, 3, 4, 5, 6, 7, 8, 9)
vals = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# create a list of random integers from <1, 100>
# calculate len, sum, min, max from the list


# create a new list of words a) having 3 letters b) starting with w or c
words = ['sky', 'blue', 'rock', 'small', 'nice', 'cup', 'war', 'tomorrow']


# read words from words.txt file and transform them into tuple, all in lowercase
```

## Riesenia

```python
# print all vowels
text = 'there are many stars in the sky'
# vowels = ["a", "e", "i", "o", "u", "y"]
vowels = 'aeiouy'

for c in text:

    if c in vowels:
        print(c)

# remove punctunation characters (?!.) from the text
text2 = 'And old falcon? Yes! Stars in the sky.'

replaced = text2.replace('!', '').replace('?', '').replace('.', '')
print(replaced)


import random

numbers = [2, 3, 1, 6, 7, 8, 3, 4, 9, 2, 9]
sample_nums = random.sample(numbers, 3)
print(sample_nums)
print(sum(sample_nums))

import funcy

# create nums2 that contains unique values
nums = [2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 9]

# nums2 = set(nums)
# nums2_l = list(nums2)
# print(nums2)
# print(nums2_l)


nums_unique = list(funcy.distinct(nums))
print(nums_unique)

# calculate sum
# transform into (1, 2, 3, 4, 5, 6, 7, 8, 9)
vals = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
mysum = 0


# for nested in vals:

#     for e in nested:
#         mysum += e


for nested in vals:
    mysum += sum(nested)

print(mysum)



import funcy

flattened = tuple(funcy.flatten(vals))
print(flattened)


import random

random_vals = []

# for loop/range, random.randint, append 

for e in range(100):
    r = random.randrange(1, 101)

    random_vals.append(r)


print(len(random_vals))
print(sum(random_vals))
print(min(random_vals))
print(max(random_vals))

print(random_vals)


# create a new list of words a) having 3 letters b) starting with w or c
words = ['sky', 'blue', 'rock', 'small', 'nice', 'cup', 'war', 'tomorrow']

# filter, len, startswith

# filter
# list comprehensions

words_3 = list(filter(lambda word: len(word) == 3, words))
print(words_3)

words_3_1 = [word for word in words if len(word) == 3]
print(words_3_1)


# words_w_c = [word for word in words if word.startswith('c') or word.startswith('w')]
words_w_c = [word for word in words if word.startswith(('c', 'w'))]
print(words_w_c)


filename = 'words.txt'
words = []

with open(filename, 'r') as fd:

    for line in fd:

        word = line.rstrip().lower()
        words.append(word)


print(words)

words_n = tuple(words)
print(words_n)
```




## Minesweeper

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 10  # 10x10 grid
CELL_SIZE = WIDTH // GRID_SIZE
MINES = 10
FONT = pygame.font.Font(None, 36)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))  # Extra space for status
pygame.display.set_caption("Minesweeper")

# Cell states
HIDDEN = 0
REVEALED = 1
FLAGGED = 2

class Minesweeper:
    def __init__(self):
        self.grid = [[HIDDEN for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.values = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.mines = set()
        self.game_over = False
        self.won = False
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        # Randomly place mines
        while len(self.mines) < MINES:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            self.mines.add((x, y))

    def calculate_numbers(self):
        # Calculate numbers based on nearby mines
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if (x, y) in self.mines:
                    self.values[y][x] = -1  # Mine
                else:
                    count = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) in self.mines:
                                count += 1
                    self.values[y][x] = count

    def reveal(self, x, y):
        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE) or self.grid[y][x] != HIDDEN:
            return
        
        self.grid[y][x] = REVEALED
        if self.values[y][x] == -1:  # Hit a mine
            self.game_over = True
            return
        elif self.values[y][x] == 0:  # Empty cell, reveal neighbors
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    self.reveal(x + dx, y + dy)

    def flag(self, x, y):
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            if self.grid[y][x] == HIDDEN:
                self.grid[y][x] = FLAGGED
            elif self.grid[y][x] == FLAGGED:
                self.grid[y][x] = HIDDEN

    def check_win(self):
        revealed_count = sum(row.count(REVEALED) for row in self.grid)
        return revealed_count == GRID_SIZE * GRID_SIZE - MINES

    def draw(self, surface):
        # Draw grid
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if self.grid[y][x] == HIDDEN:
                    pygame.draw.rect(surface, GRAY, rect)
                elif self.grid[y][x] == FLAGGED:
                    pygame.draw.rect(surface, BLUE, rect)
                    pygame.draw.polygon(surface, WHITE, 
                                      [(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4),
                                       (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE * 3 // 4),
                                       (x * CELL_SIZE + CELL_SIZE * 3 // 4, y * CELL_SIZE + CELL_SIZE // 4)], 2)
                elif self.grid[y][x] == REVEALED:
                    pygame.draw.rect(surface, WHITE, rect)
                    if self.values[y][x] == -1:
                        pygame.draw.circle(surface, RED, rect.center, CELL_SIZE // 3)
                    elif self.values[y][x] > 0:
                        text = FONT.render(str(self.values[y][x]), True, BLACK)
                        surface.blit(text, text.get_rect(center=rect.center))
                pygame.draw.rect(surface, BLACK, rect, 1)  # Grid lines

        # Draw status bar
        status_rect = pygame.Rect(0, HEIGHT, WIDTH, 50)
        pygame.draw.rect(surface, BLACK, status_rect)
        if self.game_over:
            status_text = FONT.render("Game Over! Press R to Restart", True, RED)
        elif self.won:
            status_text = FONT.render("You Won! Press R to Restart", True, BLUE)
        else:
            flags_left = MINES - sum(row.count(FLAGGED) for row in self.grid)
            status_text = FONT.render(f"Flags Left: {flags_left}", True, WHITE)
        surface.blit(status_text, status_text.get_rect(center=status_rect.center))

def main():
    clock = pygame.time.Clock()
    game = Minesweeper()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.game_over and not game.won:
                x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                if event.button == 1:  # Left click to reveal
                    game.reveal(x, y)
                elif event.button == 3:  # Right click to flag
                    game.flag(x, y)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game = Minesweeper()  # Restart game
        
        # Check win condition
        if not game.game_over and game.check_win():
            game.won = True
        
        # Draw everything
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```


## Matrix animation

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Digital Rain")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FADE_ALPHA = 13  # Equivalent to rgba(0, 0, 0, 0.05) with 255 scale (0.05 * 255 ≈ 13)

# Font setup
FONT_SIZE = 13
font = pygame.font.SysFont("MS Gothic", FONT_SIZE)

def random_katakana():
    return chr(0x30A0 + int(random.random() * 96))

# Calculate columns based on screen width and font size
COLUMNS = WIDTH // FONT_SIZE

# Adjust font size if it's too big for the screen
if COLUMNS < 10:
    FONT_SIZE = 12
drops = [0] * COLUMNS  # Starting y-position for each column

# Create a surface for fading background
fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
fade_surface.fill((0, 0, 0, FADE_ALPHA))

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply fading background
    screen.blit(fade_surface, (0, 0))

    # Draw and update drops
    for i in range(len(drops)):
        # Randomly select a character
        char = random_katakana()
        x = i * FONT_SIZE  # Calculate x position based on column index
        y = drops[i] * FONT_SIZE  # Calculate y position based on drop position

        # Render character in green with antialiasing
        text = font.render(char, True, GREEN)  # Antialiasing enabled
        text_rect = text.get_rect(topleft=(x, y))
        screen.blit(text, text_rect)

        # Increment drop position
        drops[i] += 1

        # Adjust the reset condition to be slightly more frequent
        if y > HEIGHT and random.random() > 0.95:
            drops[i] = random.randint(-20, 0)
        # Reset drop if it goes off-screen with a small random chance
        if y > HEIGHT and random.random() > 0.975:
            drops[i] = 0

    # Update display
    pygame.display.flip()
    clock.tick(20)  # 20 FPS (~50ms interval like JS setInterval)

# Quit Pygame
pygame.quit()
```


## 17. riadok tabulky

```python
from selectolax.parser import HTMLParser

import requests 

url = 'https://webcode.me/countries.html'

r = requests.get(url)
html = r.text

tree = HTMLParser(html)

n  = 17

nth_p = tree.css(f'tr:nth-child({n})')
print(nth_p)
if nth_p:
    print(f"row {n}: {nth_p[0].text().strip()}")
else:
    print(f"No row found at position {n}")
```



## read JSON from webpage

```python
import requests


url = 'https://webcode.me/users.json'

resp = requests.get(url)
content = resp.json()

print(content)
print(type(content))

for user in content['users']:

    print(user['first_name'])
    print(user['last_name'])
    print(user['email'])

    print('--------------------------------')
```


## Multiple JSON users

```python
import json

data = [
    {"name": "Jane", "age": 17},
    {"name": "Mike", "age": 23},
    {"name": "Sarah", "age": 19},
    {"name": "Tom", "age": 25},
    {"name": "Emily", "age": 21},
    {"name": "Alex", "age": 28},
    {"name": "Lisa", "age": 20},
    {"name": "John", "age": 24},
    {"name": "Kelly", "age": 18},
    {"name": "David", "age": 27},
    {"name": "Anna", "age": 22},
    {"name": "Peter", "age": 26},
    {"name": "Rachel", "age": 19},
    {"name": "Mark", "age": 30},
    {"name": "Julia", "age": 21},
    {"name": "Ben", "age": 23},
    {"name": "Sophie", "age": 20},
    {"name": "Chris", "age": 25},
    {"name": "Laura", "age": 18},
    {"name": "James", "age": 29},
    {"name": "Emma", "age": 22}
]

fname = 'friends.json'
with open(fname, 'w') as f:
    json.dump(data, f)
```



















## read words

```python
words = []

filename = 'words.txt'

with open(filename) as fd:

   for line in fd:
      cleaned_line = line.strip()
      words.append(cleaned_line)

print(words)
words.sort()
print(words)
```


## reverse vs reversed

```python
numbers = [4, 3, 6, 1, 2, 0, 5]

print(numbers)
numbers.reverse()
print(numbers)

print('--------------------------------')

numbers2 = (-4, 3, 16, 11, 21, 0, -5)
numbers2_reversed = tuple(reversed(numbers2))
print(numbers2_reversed)
print(numbers2)
```


## sort vs sorted

```python
numbers = [4, 3, 6, 1, 2, 0, 5]

print(numbers)
numbers.sort()
print(numbers)

print('--------------------------------')

numbers2 = (-4, 3, 16, 11, 21, 0, -5)
numbers2_sorted = sorted(numbers2)
print(numbers2_sorted)
print(numbers2)
```


## jednotkova ntica

```python
x = (3 + 5) * 6
print(x)

n = (556,)
print(type(n))

n = (550) * 1 
print(type(n))
```


## vypis 11

```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```


## type function

```python
items = (True, 'sky', 0, 2.3, (), 'war', [12, 11, 6], 2, 3, None)

for item in items:
   if type(item) == int:
      print(item)
```

## Decimal

```python
from decimal import Decimal

x = 0.1 + 0.1 + 0.1

print(x == 0.3)
print(x)

print("----------------------")

x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')

print(x == Decimal('0.3'))
print(float(x) == 0.3)
print(x)
```


## calculate sum

```python
nums = "1,5,6,8,2,3,1,9"

fields = nums.split(",")
print(fields)

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)

mysum = sum(map(int, nums.split(',')))
print(mysum)
```


## calculate sum from string of CSV data

```python
nums = "1,5,6,8,2,3,1,9"

fields = nums.split(",")
print(fields)

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```



## String indexing

```python
msg = 'and old falcon in the sky'

print(msg[8:14])
print(msg[22:25])
print(msg[-3:])
```



## String formatting

```python
name = 'Peter'
age = 23
occupation = 'student' # and he is a student

print('%s is %d years old and he is a %s' % (name, age, occupation))
print('{} is {} years old and he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old and he is a {occupation}')
```



## Tkiter application

```python
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib import style


def create_chart():
    # Set the style
    style.use('ggplot')

    # Data
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]

    # Create the bar chart
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')

    # Add labels and title
    plt.title('Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')

    # Save the chart
    # plt.savefig('barchart.png')
    plt.show()
    # Close the plot to free memory
    plt.close()

    # Optional: Update a label to show the chart was generated
    status_label.config(text="Chart generated and saved as 'barchart.png'")


# Create the main window
root = tk.Tk()
root.title("Chart Generator")
root.geometry("300x200")

# Create a button
generate_button = tk.Button(root,
                            text="Generate Chart",
                            command=create_chart,
                            padx=10,
                            pady=5)
generate_button.pack(pady=20)

# Create a status label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Start the application
root.mainloop()
```



## for with break

```python
import random

for num in range(1000_000):

    r = random.randint(0, 30)

    print(r, end=' ')

    if r == 22:
        break

print()
```


## range/list/tuple

```python
for n in range(10, 56, 5):
    print(n)

print(range(10, 56, 5))

vals = list(range(10, 56, 5))
print(vals)

vals = tuple(range(10, 56, 5))
print(vals)
```



## Opakovanie

```python
# print message: John Doe is 34 years old and he is a gardener
name = "John Doe"
age = 34
occupation = 'gardener'

# calculate sum using for/while loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# calculate minimum, maximum, number of els, sum, mean
# use functions
vals2 = [1, -2, 13, 24, 5, 9]

# read the words.txt file and print all words in uppercase
```

## Riesenia

```python
import statistics


# print message: John Doe is 34 years old and he is a gardener
name = "John Doe"
age = 34
occupation = 'gardener'

msg = name + ' is ' + str(age) + ' years old and he is a ' + occupation
print(msg)

# calculate sum using for/while loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0
for val in vals:
    mysum += val

print('the sum is', mysum)

# calculate minimum, maximum, number of els, sum, mean
# use functions
vals2 = [1, -2, 13, 24, 5, 9]
print(min(vals2))
print(max(vals2))
print(len(vals2))
print(sum(vals2))

print(sum(vals2)/len(vals2))
print(statistics.mean(vals2))

filename = 'words.txt'

with open(filename, 'r') as fd:
    for line in fd:
        print(line.strip().upper())
```


## fstrings

```python
name = "John Doe"
age = 34
occupation = 'gardener'

msg = f'{name} is {age} years old and he is a {occupation}'
print(msg)
```




## open function

```python
filename = 'words.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    # print(repr(content))

    words = content.split()
    print(words)


print('task ...')
```

```python
filename = 'words.txt'

with open(filename, 'r') as file:

    lines = file.readlines()
    print(lines)

    for line in lines:
        print(line.strip())

print('finished')
```

```python
filename = 'words.txt'

with open(filename, 'r') as file:

    for line in file:
        print(line.strip())

print('finished')
```


## not in operator

```python
vals = [1, 2, 3, 4, 5]

print(6 not in vals)
```


## input & repr

```python
x = input('enter x value: ')
y = input('enter y value: ')

print(repr(x))
print(repr(y))

print(int(x) + int(y))
```


## Type casting

```python
n = 6
word = 'falcon'

# 6 -> '6'
print(str(n) + ' ' + word + 's')
```

```python
x = '6'
y = '8'

# string addition
print(x + y)

# integer addition
# type casting to int
print(int(x) + int(y))
```

## Operators

```python
print(5 // 2)
print(5 / 2)
print(5 % 2)

print(10 ** 3)
print(pow(10, 3))
```


## Builtins & statistics

```python
import statistics

vals = [9, -2, -3, 4, 0, 1, 5, 16]

print(sum(vals))
print(len(vals))
print(min(vals))
print(max(vals))

word = 'falcon'
print(len(word))

print(abs(5))
print(abs(-5))

sorted_vals = sorted(vals)
print(sorted_vals)
print(vals)

print(statistics.mean(vals))
print(statistics.median(vals))
```


## For cycle

```python
mysum = 0
numbers = [1, 2, 3, 4, 5, 6]

# print(sum(vals))

for number in numbers:
    mysum = mysum + number

print('the sum of values is: ', mysum)
print('finished')

words = ['sky', 'towel', 'pen', 'rock']

for word in words:
    print(word.upper())
```


## While cycle

```python
msg = 'an old falcon'

i = 0

while i < 7:
    print(msg)

    i = i + 1

print('program finished')
```


## Podmienky

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')

if r < 0:
    print('The r variable is negative')

if r == 0:
    print('The r variable is zero')
```

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('The r variable is negative')
else:
    print('The r variable is zero')
```

















## SQL for users

```sql
CREATE TABLE users(id serial PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), city VARCHAR(255));
```

## Dataclass


```python
import csv
from dataclasses import dataclass

# Define the User dataclass
@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    city: str

# List to store User instances
users = []

# Read the CSV file

with open('users.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Convert the row into a User instance
        # Ensure id is converted to int, others remain strings
        user = User(
            id=int(row[0]),
            first_name=row[1],
            last_name=row[2],
            city=row[3]
        )
        users.append(user)

# Print all users to verify
for user in users[:11]:
    print(user)
```




## Fake data generation

```python
from faker import Faker

faker = Faker()
filename = 'users.csv'

with open(filename, 'w') as fd:

    for idx in range(1, 10_001):
        first_name = faker.first_name()
        last_name = faker.last_name()
        city = faker.city()

        fd.write(f'{idx},{first_name},{last_name},{city}\n')
```



## Dataclass

```python
from dataclasses import dataclass

@dataclass()
class User:
    first_name: str
    last_name: str
    email: str


users = [
    User('John', 'Doe', 'john.doe@example.com'),
    User('Roger', 'Roe', 'roger.roe@example.com'),
    User('Lucy', 'Smith', 'lucy.smith@example.com'),
]

for user in users:
    print(user)
```

## Without dataclass

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        # Mimics dataclass default string representation
        return f"User(first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"


# Create list of User instances
users = [
    User('John', 'Doe', 'john.doe@example.com'),
    User('Roger', 'Roe', 'roger.roe@example.com'),
    User('Lucy', 'Smith', 'lucy.smith@example.com'),
]

# Print each user
for user in users:
    print(user)
```


## Opakovanie

```python
# transform this list to a list of positive values
vals = [2, -3, -1, 0, 2, 3, 9, 3, -9]

# filter out all words ending in 'l'
words = ['sky', 'war', 'portal', 'earth', 'small']

# filter all words that have r character
words2 = ['spy', 'rust', 'tomorrow', 'water', 'war', 'cup']

# read words from 'words.txt' file, remove new lines and sort them
```


The `words.txt` file:

```
sky
word
out
blue
war
cup
soup
food
```

## Riesenia

```python
# transform this list to a list of positive values
vals = [2, -3, -1, 0, 2, 3, 9, 3, -9]

# def transform(e):
#     if e < 0:
#         return -e
#     else:
#         return e


vals2 = list(map(abs, vals))
print(vals2)

# filter out all words ending in 'l'
words = ['sky', 'war', 'portal', 'earth', 'small']
# words_l = list(filter(lambda word: word.endswith('l'), words))
words_l = list(filter(lambda word: word[-1] == 'l', words))
print(words_l)

words2 = ['spy', 'rust', 'tomorrow', 'water', 'war', 'cup']

words2_r = list(filter(lambda word: 'r' in word, words2))
print(words2_r)

words2_r = list(filter(lambda word: word.find('r') != -1, words2))
print(words2_r)

# read words from 'words.txt' file, remove new lines and sort them

filename = 'words.txt'
words = []
with open(filename, 'r') as fd:

    for line in fd:
        words.append(line.strip())

print(words)
words.sort()
print(words)
```



## Pandas


```python
import pandas as pd

filename = 'data.csv'

df = pd.read_csv(filename, header=None)
total_sum = df.values.sum()  # Sum all elements
print("Total sum of all values:", total_sum)
```


## sum values

```python
# calculate sum, without for loop
data = '1,2,3,4,5,6,7,8,9,10'

# fields = data.split(',')
# print(fields)

suma = sum(map(int, data.split(',')))
print(suma)
```


## filter words starting with w/W

```python
# filter all words starting with 'w'
words = ['sky', 'warm', 'blue', 'nord', 'war', 'water', 'Wrong', 'Wrath']

# words_w = list(filter(lambda word: word.lower().startswith('w'), words))
# words_w = list(filter(lambda word: word.startswith('w') or word.startswith('W'), words))
# words_w = list(filter(lambda word: word.startswith(('w', 'W')), words))
words_w = list(filter(lambda word: word[0] == 'W' or word[0] == 'w', words))

print(words_w)
```


## map function

```python
def twice(e):
    return 2 * e

def cube(e):
    return e * e * e

vals = [-2, 3, 0, 9, -1, 3, -5]
vals2 = list(map(twice, vals))
vals3 = list(map(cube, vals))

print(vals2)
print(vals3)
print(vals)

# vals2 = []
#
# for val in vals:
#     vals2.append(val * 2)

# print(vals2)

words = ['sky', 'blue', 'nord', 'war', 'water']

def to_title(e):
    return e.title()


# words_titled = list(map(lambda e: e.title(), words))
words_titled = list(map(to_title, words))
print(words_titled)
```

## map with lambdas

```python
vals = [-2, 3, 0, 9, -1, 3, -5]
vals2 = list(map(lambda e: e * 2, vals))
vals3 = list(map(lambda e: e * e * e, vals))

print(vals2)
print(vals3)
print(vals)

words = ['sky', 'blue', 'nord', 'war', 'water']

words_titled = list(map(lambda e: e.title(), words))
print(words_titled)

words_uppered = list(map(lambda e: e.upper(), words))
print(words_uppered)
```


## filter function

```python
vals = [-2, 3, 0, 9, -1, 3, -5]

def is_negative(e):
    if e < 0:
        return True

def is_positive(e):
    if e > 0:
        return True

negatives = list(filter(is_negative, vals))
print(negatives)

positives = list(filter(is_positive, vals))
print(positives)

def has3chars(e):
    if len(e) == 3:
        return True

words = ['sky', 'blue', 'nord', 'war', 'water']

words_3 = list(filter(has3chars, words))
print(words_3)
```

## Lambda functions with filter

```python
vals = [-2, 3, 0, 9, -1, 3, -5]

negatives = list(filter(lambda e: e < 0, vals))
print(negatives)

positives = list(filter(lambda e: e > 0, vals))
print(positives)

words = ['sky', 'blue', 'nord', 'war', 'water']

words_3 = list(filter(lambda word: len(word) == 3, words))
print(words_3)
```


## Chart for GDP of EU countries 

```python
import matplotlib.pyplot as plt

countries = [
    'Germany', 'France', 'Italy', 'Spain', 'Netherlands', 'Poland', 'Belgium',
    'Sweden', 'Ireland', 'Austria', 'Denmark', 'Romania', 'Czech Republic',
    'Finland', 'Portugal', 'Greece', 'Hungary', 'Slovakia', 'Bulgaria',
    'Luxembourg', 'Croatia', 'Lithuania', 'Slovenia', 'Latvia', 'Estonia',
    'Cyprus', 'Malta'
]

gdp = [4526, 3052, 2301, 1620, 1154, 809, 645, 585, 551, 512, 407, 351, 343,
       296, 289, 244, 212, 133, 102, 85.76, 84.39, 79.79, 69.15, 42.25, 41.29,
       33.89, 22.33]

data = list(zip(countries, gdp))
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
sorted_countries, sorted_gdp = zip(*sorted_data)

plt.figure(figsize=(10, 15))
plt.barh(sorted_countries, sorted_gdp)
plt.title('GDP of European Union Countries (USD Billion) as of December 2023')
plt.ylabel('Country')
plt.xlabel('GDP (USD Billion)')
plt.grid(axis='x')
plt.show()
```




## Write to Documents directory

```python
filename = "C:\\Users\\bodnar\\Documents\\words2.txt"
words = ['sky', 'loop', 'nice', 'town', 'up']

with open(filename, 'a') as fd:

    for word in words:
        fd.write(f'{word}\n')
```




## append to file

```python
filename = 'words2.txt'
words = ['sky', 'loop', 'nice', 'town', 'up']

with open(filename, 'a') as fd:

    for word in words:
        fd.write(f'{word}\n')
```


## write to file

```python
filename = 'words2.txt'
words = ['sky', 'loop', 'nice', 'town', 'up']

with open(filename, 'w') as fd:

    for word in words:
        fd.write(f'{word}\n')
```



## Read words 

The 'words.txt' file:  

```
sky
word
out
blue
war
cup
soup
food
```


```python
filename = 'words.txt'
cleaned_words = []

with open(filename) as fd:

    for line in fd:
        cleaned_words.append(line.strip())

print(cleaned_words)
````





## Opakovanie


```python
# vypis 'John Doe is a gardener and is 45 years old', pouzi fstring
name = 'John Doe'
occupation = 'gardener'
age = 45

# calculate sum using for loop
vals = [2, 1, 3, 5, 4]

# calculate sum
data = '1,2,3,4,5,6,7,8,9,10'

# print negative values
vals2 = [4, -5, 2, -1, -9, 0, 5, 7, -3]

# print all strings
data2 = [True, 10, 0.1, -3, None, (2, 3), 'falcon', {3, 4},
         False, 'bark', 9.3, ]

# create a list of 100 random numbers
```


## Riesenia

```python
# vypis 'John Doe is a gardener and is 45 years old'
name = 'John Doe'
occupation = 'gardener'
age = 45

msg = f'{name} is a {occupation} and is {age} years old'
print(msg)

# calculate sum using for loop
vals = ['2', '1', '3', '5', '4']
# print(sum(vals))

mysum = 0

for e in vals:
    mysum += int(e)

print(mysum)



data = '1,2,3,4,5,6,7,8,9,10'
fields = data.split(',')
print(fields)
mysum = 0

for e in fields:
    mysum += int(e)

print(mysum)


vals2 = [4, -5, 2, -1, -9, 0, 5, 7, -3]

for val in vals2:
    if val < 0:
        print(val)

data2 = [True, 10, 0.1, -3, None, (2, 3), 'falcon', {3, 4},
         False, 'bark', 9.3 ]

print(type(3))

for val in data2:
    if type(val) == str:
        print(val)



import random

randvals = []

for e in range(1, 101):
    r = random.randint(1, 101)
    randvals.append(r)

print(len(randvals))
print(randvals[:11])
print(randvals[-11:])

```





















## Finish

```python
# calculate the sum of all letters
words = ['sky', 'cup', 'forest', 'rock']

# calculate the sum of all values
vals = ((1, 2, 3), (4, 5, 6))

# calculate the sum of positive values
vals2 = [-3, -4, 0, 1, 2, -9, 11, 12, 9]

# split and sort the words
data = 'sky blue rocket war water pen black'
```


```python

# calculate the sum of all letters
# for loop, len, mysum
words = ['sky', 'cup', 'forest', 'rock']
mysum = 0

for word in words:
    mysum += len(word)

print(mysum)


# calculate the sum of all values
# for loop, mysum, sum
vals = (
    (1, 2, 3),
    (4, 5, 6)
)
mysum = 0

for nested in vals:
    mysum += sum(nested)

print(mysum)

# calculate the sum of positive values
# for loop, mysum, if condition
vals2 = [-3, -4, 0, 1, 2, -9, 11, 12, 9]

mysum = 0

for val in vals2:
    if val > 0:
        mysum += val

print(mysum)

# split and sort the words
# split sort
data = 'sky blue rocket war water pen black'

words = data.split()
words.sort()
print(words)
```





## Dictionaries

```python
words = { 'girl': 'Maedchen', 'house': 'Haus', 'death': 'Tod' }
print(words)

words['car'] = 'Wagen'
print(words)

words['house'] = 'das Haus'
print(words)
```


## typle/list

```python
data = []

# nacitavame data
data = [1, 2, 3, 4, 5, 6]

ndata = tuple(data)
print(ndata)
```


## Sorting data

```python
numbers = [4, 3, 6, 1, 2, 0, 5]

print(numbers)
# inplace sorting
numbers.sort()
print(numbers)

print('----------------------------')
print('----------------------------')

vals = [5, 3, 0, 1, 2, 4]
sorted_vals = sorted(vals)
print(sorted_vals)
print(vals)
```

## Nested tuples

```python
# print value 11 using index operation
data = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```

```python
# print value 11 using index operation
data = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))

print(data)
print(data[3][3][3][1])
```


## calculate sum of CSV values

```python
data = '1,2,3,4,5,6,7,8,9,10'

fields = data.split(',')
print(fields)

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```


```python
text = "He said: \"there are many stars\""
print(text)

text = 'He said: "there are many stars"'
print(text)

text = 'this was a \'great\' movie'
print(text)

text = "this was a 'great' movie"
print(text)
```



## Opakovanie

```python
name = "Peter"
print(name)
print(type(name))

age = 56
print(age)
print(type(age))

vals = (1, 2, 3)
print(type(vals))

vals2 = [4, 5, 6]
print(type(vals2))
```

```python
# create a fstring message from variables:
# 'John Doe is a driver and lives in New York'
name = 'John Doe'
occupation = 'driver'
city = 'New York'

# print values using loop
# print the count of the values
vals = [3, 4, 5, 6, 3, 5, 9, 10]

# print the string 6 times
word = 'falcon'

# print positive values
# use for loop and if condition
vals2 = (-3, 4, 0, 5, 9, -2, -1, 9, 11, -2)
```

## Riesenia

```python

# create a fstring message from variables:
# 'John Doe is a driver and lives in New York'
name = 'John Doe'
occupation = 'driver'
city = 'New York'

print(f'{name} is a {occupation} and lives in {city}')

# print values using loop
# print the count of the values
vals = [3, 4, 5, 6, 3, 5, 9, 10]

for element in vals:
    print(element)

print(len(vals))

# print the string 6 times
word = 'falcon'

# print(word * 6)
for i in range(6):
    print(word, end=' ')


# print positive values
# use for loop and if condition
vals2 = (-3, 4, 0, 5, 9, -2, -1, 9, 11, -2)

for val in vals2:
    if val > 0:
        print(val)
```




```python
name = 'Roger Roe'
age = 35
job = 'programmer'

# msg = name + ' is ' + str(age) + ' years old ' + ' he is a ' + job
msg = f'{name} is {age} years old, he is a {job}'

print(msg)
```



```python
vals = [1, 2, 3, 4, 5]
val = 3

if val in vals:
    print('inside: ', val)

val2 = 11
if val2 not in vals:
    print('not inside: ', val2)
```


```python
vals = [1, 2, -3, 4, -5, 6, 7, 8, -9, -10, -12]

for val in vals:

    if val % 2 == 0 and val > 0:
        print(val)
```


```python
x = '3'
y = '4'

print(int(x) + int(y))
```

```python
n = 3

n_s = str(n)
word = 'coffees'

msg = n_s + word
print(msg)
```


```python
words = ['sky', 'storm', 'worm', 'war']

for word in words:
    print(word, len(word))

print(len(words))
```


```python
word = 'falcon'

i = 0

while i < 3:
    print(word)
    i = i + 1

print('end')
```







## AI analyzing

```python
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


file_name = 'typescript_arrays.html'

# llama-3.3-70b-versatile
# mixtral-8x7b-32768
# deepseek-r1-distill-llama-70b
model = 'mixtral-8x7b-32768'

with open(file_name, 'r') as file:
    html_template = file.read()

content = f'''Write a TypeScript tutorial that convers the Union type.
In paragraphs, try to limit the sentences to 80 chars. Don't use hello world.
Output in HTML.
'''

content += f"Use this HTML template as a reference: {html_template}"


messages = [
    {'role': 'user', 'content': content},
]

print(model)
# exit

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    temperature=0.7,
    top_p=0.9,
    model=model,
    max_completion_tokens=32768
)

print(chat_completion.choices[0].message.content)
```



## filter users by last name

```python
import csv

file_name = 'users.csv'
users = []


with open(file_name, 'r') as f:

    reader = csv.DictReader(f)

    for line in reader:
        users.append(line)


users_w = [user for user in users if user['last_name'].startswith('W')]

print(len(users_w))

for user in users_w[:50]:
    print(user)
```




## Print first 20 with tablib

```python
import tablib

ds = tablib.Dataset()

fname = 'users.csv'
with open(fname, 'r') as f:

    ds.load(f)

for user in ds[:21]:
    print(user)
```


## Generate fake users

```python
from faker import Faker

faker = Faker()

with open("users.csv", "w") as f:

    f.write("first_name,last_name,email\n")

    for _ in range(1_500_000):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        f.write(f"{first_name},{last_name},{email}\n")

        # if _ % 1_000 == 0:
        #     print(f"Done {_}")

    print("Done")
```



## The __str__ function for User

```python

class Circle:

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"


c = Circle()
print(c)

c.setRadius(5)
print(c)
```

## Object identity

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __eq__(self, other):
    #     if isinstance(other, User):
    #         return self.name == other.name and self.age == other.age
    #     return False

u1 = u11 =  User("John Doe", 35)
u2 = User("John Doe", 35)

print(id(u1))
print(id(u2))

print(u1 == u2)
print(u1 == u11)
```


## Pandas show all data

```python
import pandas as pd

# Load your dataset
titanic_df = pd.read_csv('titanic.csv')

# Set the option to display all rows
pd.set_option('display.max_rows', None)

# Display the dataframe
print(titanic_df)
```








## Pycharm cheat sheet

https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf


## filter words from URL 

```python
import requests


# with list comprehension, filter words having
# 3 characters len(word) == 3

url = 'https://webcode.me/words.txt'

resp = requests.get(url)

# print(resp.headers)
# print(resp.status_code)
# print(resp.text)
print(repr(resp.text))

content = resp.text
content2 = content.strip()

words = content2.split()
print(words)

words_3 = [word for word in words if len(word) == 3]
print(words_3)
```


## filter words from local file

```python
# with list comprehension, filter words having
# 3 characters len(word) == 3

filename = 'words.txt'


with open(filename, 'r') as fd:
    lines = fd.readlines()
    print(lines)

    words_3 = [line.strip().upper() for line in lines if len(line.strip()) == 3]
    print(words_3)
```


## Vowels & consonants

```python
def is_vowel(c):

    vowels = 'aeiouAEIOU'

    if c in vowels:
        return True
    else:
        return False

def is_consonant(c):

    vowels = 'aeiouAEIOU .'

    if c not in vowels:
        return True
    else:
        return False


sentence = 'There are eagles in the sky.'

vowels = [c for c in sentence if is_vowel(c)]
print(vowels)

consonants = [c for c in sentence if is_consonant(c)]
print(consonants)
```



## Filtering by list comprehensions

```python
vals = [2, 2.3, 'sky', True, (), (1, 2, 3), 'war', 'cup']

strings = [val for val in vals if type(val) == str]
print(strings)

tuples = [val for val in vals if type(val) == tuple]
print(tuples)
```



Sure! Here is a table of common Python `datetime` format specifiers:

| Format | Description                | Example             |
|--------|----------------------------|---------------------|
| `%Y`   | Year with century          | `2025`              |
| `%y`   | Year without century       | `25`                |
| `%m`   | Month (zero-padded)        | `02`                |
| `%B`   | Full month name            | `February`          |
| `%b`   | Abbreviated month name     | `Feb`               |
| `%d`   | Day of the month (zero-padded) | `25`            |
| `%H`   | Hour (24-hour clock, zero-padded) | `16`        |
| `%I`   | Hour (12-hour clock, zero-padded) | `04`        |
| `%p`   | AM/PM                      | `PM`                |
| `%M`   | Minute (zero-padded)       | `11`                |
| `%S`   | Second (zero-padded)       | `59`                |
| `%f`   | Microsecond                | `123456`            |
| `%A`   | Full weekday name          | `Tuesday`           |
| `%a`   | Abbreviated weekday name   | `Tue`               |
| `%w`   | Weekday as a number (0=Sunday) | `2`            |
| `%j`   | Day of the year (zero-padded) | `056`           |
| `%U`   | Week number of the year (Sunday as first day of the week, zero-padded) | `08`  |
| `%W`   | Week number of the year (Monday as first day of the week, zero-padded) | `08`  |
| `%c`   | Locale's appropriate date and time representation | `Tue Feb 25 16:11:59 2025` |
| `%x`   | Locale's appropriate date representation | `02/25/25` |
| `%X`   | Locale's appropriate time representation | `16:11:59` |
| `%%`   | A literal `%` character    | `%`                 |

These format specifiers can be used with the `strftime` method to format `datetime` objects as strings:




# Opakovanie

the words.txt file:

```
sky
blue
rock
pen
water
war 
cloud
cup
```

```python
#  print message

name = 'John Doe'
age = 34

# filter positive values

vals = [-2, 3, 0, 9, -2, 11, 9, -5]

# calculate sum from data

data = '1,2,3,4,5,6,7,8,9,10' 

# read words and select those starting with 'w'

filename = 'words.txt'
```

## Riesenia

```python
#  print message, with fstring

# name = 'John Doe'
# age = 34

# msg = f'{name} is {age} years old'
# print(msg)

# filter positive values

def is_positive(x):
    return x > 0


vals = [-2, 3, 0, 9, -2, 11, 9, -5]

#positive = list(filter(is_positive, vals))
positive = list(filter(lambda x: x > 0, vals))
print(positive)

for neg in filter(lambda x: x < 0, vals):
    print(neg)
```

```python
filename = 'words.txt'

with open(filename, 'r') as fd:
    rows = fd.readlines()
    rows2 = list(map(lambda e: e.strip(), rows))

    words_w = list(filter(lambda e: e.startswith('w'), rows2))
    print(words_w)
```



```python
# calculate sum from data

data = '1,2,3,4,5,6,7,8,9,10' 
fields = data.split(',')
print(fields)

# 1)

mysum = 0
for field in fields:
    # mysum = mysum + int(field)
    mysum += int(field)

print(mysum)

# 2) map

print(sum(map(int, fields)))
```











# Priklady


`properties.csv`:

```
428000
365000
444000
389500
365000
415000
1
271000
415000
415000
449000
415000
328000
382100
240000
340000
415000
355000
450000
339000
359900
279900
330000
284800
285000
429900
419900
459950
460000
333000
280710
236000
399990
356000
339000
249000
318100
337999
339000
339000
405900
369800
379000
355000
279900
286900
379990
399990
259900
230000
249800
469000
379999
499999
330000
219900
349990
343000
340000
276000
345000
322380
345000
345000
345000
245897
239900
259000
269000
345000
360000
270000
275000
279000
260000
259000
223000
229900
224990
307500
264500
269500
320000
264500
320000
264900
255000
220000
230000
223000
279990
263000
279990
299900
220000
239000
263999
259000
229089
263681.25
289900
245000
250766.25
259000
289990
252000
289000
229000
219990
215000
215000
245000
199000
192000
285000
283147
249000
339900
179000
189900
221350
189900
239900
229900
245000
204000
295000
254900
249000
264900
255000
278100
239000
299000
229900
184900
239000
211992
253000
239000
254000
256390
299900
405500
427450
199000
235000
229990
235000
216000
229990
229000
230000
275000
255000
249999
243000
280000
415000
249000
215000
229990
240000
235000
229990
235000
240000
229000
210000
210000
244800
233000
189000
259000
224990
240000
229990
290900
295000
265000
319000
290000
249000
180000
182000
235870
183500
230000
165000
240000
185900
210000
225000
192900
168000
190000
192000
199000
389000
419990
10500
54000
12050
123
5225
9400
1240
0
1
x
123
400
450
12500
95000
45900
44000
1250000
957000
```

```python
with open(filename, 'r') as f:

    text = f.read()
    lines = text.split()

    filtered_data = [int(item) for item in lines if item.isdigit()]
    cleaned_data = [e for e in filtered_data if e > 10]

    print(cleaned_data)

    print(statistics.mean(cleaned_data))
    print(statistics.median(cleaned_data))
```





## Clean words

```python
import re
filename = 'data.txt'

with open(filename, 'r') as f:

    text = f.read()
    pattern = re.compile(r'[,;.]')

    text_cleaned = re.sub(pattern, '', text)
    words = text_cleaned.split()
    print(words)
```


```python
import re


words = ['sky  ', '\t\twar', 'water\n\n', '\t\ncup', 'sky']
cleaned = []
pattern = re.compile(r'\s+')

for word in words:

    cleaned_word = re.sub(pattern, '', word)
    cleaned.append(cleaned_word)

print(words)
print(cleaned)
```


## Split by two chars

```python
import re

data = '1,2,3;4;5,6,7;8;9;10'

pattern = re.compile(r'[;,]')
vals = re.split(pattern, data)

print(sum(map(int, vals)))
```




`users.csv`:

```csv
date_of_birth,first_name,last_name
1987,John,Doe
1996,Jane,Doe
1977,Robert,Brown
2002,Lucia,Smith
1994,Patrick,Dempsey
```

```python
import csv

filename = "users.csv"
users = []

with open(filename, "r") as f:

    reader = csv.DictReader(f)

    for row in reader:
        users.append(row)


users.sort(reverse=True, key=lambda e: e["last_name"])

for user in users:
    print(user)

print("--------------------------------------------")

users.sort(reverse=True, key=lambda e: e["date_of_birth"])

for user in users:
    print(user)
```


```python
import csv

# Read the CSV file
with open("users.csv", mode="r") as file:
    reader = csv.DictReader(file)
    users = list(reader)  # Convert the CSV data into a list of dictionaries

    
# Sort the users by last_name
sorted_users = sorted(users, key=lambda x: x["last_name"])

# Print the sorted data
print("date_of_birth,first_name,last_name")  # Print the header
for user in sorted_users:
    print(f"{user['date_of_birth']},{user['first_name']},{user['last_name']}")
```



## Opakovanie

`data.txt`:

```
I quickly followed suit, and descending into the bar-room accosted the grinning 
landlord very pleasantly. I cherished no malice towards him, though he had been 
skylarking with me not a little in the matter of my bedfellow.
However, a good laugh is a mighty good thing, and rather too scarce a good thing; 
the more’s the pity. So, if any one man, in his own proper person, afford stuff for 
a good joke to anybody, let him not be backward, but let him cheerfully allow himself 
to spend and be spent in that way. And the man that has anything bountifully laughable 
about him, be sure there is more in that man than you perhaps think for.
```


```python
import somelib

words = ['sky', 'dout', 'war', 'pike', 'now', 'teen']
words3, words4 = ...

assert words3 == ['sky', 'war', 'now'] and words4 == ['dout', 'pike', 'teen'], 'failed'
print('passed')

# ----------------------------------------------------------

import requests

url = 'https://webcode.me/words.txt'
...

number_of_words = ...


assert number_of_words == 26, 'failed'
print('passed')


# ----------------------------------------------------------

filename = 'data.txt'

with open(filename, 'r') as f:
    ...
    number_of_words = ...

assert number_of_words == 117, 'failed'
print('passed')

# ----------------------------------------------------------


# write script that reads data from 
# https://webcode.me/users.xml, use copilot
```


Riesenia:

```python
import funcy

words = ['sky', 'dout', 'war', 'pike', 'now', 'teen']
# words3 = [word for word in words if len(word) == 3]
# words4 = [word for word in words if len(word) == 4]
words3, words4 = funcy.split(lambda word: len(word) == 3, words)

words3 = list(words3)
words4 = list(words4)

assert words3 == ['sky', 'war', 'now'] and words4 == ['dout', 'pike', 'teen'], 'failed'
print('passed')
```

```python
import requests

url = 'https://webcode.me/words.txt'

resp = requests.get(url)
text = resp.text
words = text.split()

number_of_words = len(words)


assert number_of_words == 26, 'failed'
print('passed')
```


```python
filename = 'data.txt'

with open(filename, 'r') as f:
    text = f.read()
    words = text.split()
    number_of_words = len(words)


assert number_of_words == 117, 'failed'
print('passed')
````

```python
import requests
import xml.etree.ElementTree as ET

# URL of the XML data
url = 'https://webcode.me/users.xml'

# Fetch the XML data
response = requests.get(url)
xml_data = response.content

# Parse the XML data
root = ET.fromstring(xml_data)

# Define the namespace
namespace = {'ns': 'zetcode.com'}

# Iterate through each user and print their details
for user in root.findall('ns:user', namespace):
    user_id = user.get('id')
    firstname = user.find('ns:firstname', namespace).text
    lastname = user.find('ns:lastname', namespace).text
    occupation = user.find('ns:occupation', namespace).text
    
    print(f'User ID: {user_id}')
    print(f'First Name: {firstname}')
    print(f'Last Name: {lastname}')
    print(f'Occupation: {occupation}')
    print('---')
```




## fetch CSV data

```python
import requests
import csv


def dowload_data():

    url = 'https://webcode.me/users.csv'

    resp = requests.get(url)
    data = resp.text

    filename = 'users3.csv'
    with open(filename, 'w') as f:

        f.write(data)


def read_users():

    users = []

    filename = 'users3.csv'
    with open(filename, 'r') as f:

        reader = csv.DictReader(f)

        for line in reader:
            users.append(line)


    print(users[:11])

# dowload_data()
read_users()
```



## Generate users.csv

```python
import faker

fake = faker.Faker()

filename = 'users.csv'

with open(filename, 'w') as f:

    header = 'first_name,last_name,email,salary\n'
    f.write(header)

    for _ in range(1000):

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        salary = fake.random_int(850, 5500, 50)

        row = f'{first_name},{last_name},{email},{salary}\n'
        f.write(row)
```

## Basic stats

```python
import csv
import statistics

salaries = []

with open('users.csv', 'r') as f:

    reader = csv.DictReader(f)
    total_salaries = 0

    for row in reader:
        salary = int(row['salary'])
        total_salaries += salary
        salaries.append(salary)

# print(salaries)
print('total:', total_salaries)
print('count:', len(salaries))
print('max:', max(salaries))
print('min:', min(salaries))
print('average:', statistics.mean(salaries))
print('median:',statistics.median(salaries))
```


## Opakovanie

```csv
John,Doe,gardener
Roger,Roe,driver
Paul,Smith,programmer
```


```python
vals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vals2 = ...

assert vals2 == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'failed'
print('passed')

# ------------------------------------------
data = [1, 2.3, True, 'falcon', 4, -2, False, (1, 2, 3), 9]

data2 = ...

assert data2 == (-2, 1, 4, 9), 'failed'
print('passed')

# ------------------------------------------

data = '1,2,3,4,5,6,7,8,9,10'

data2 = ...

assert data2 == '10;9;8;7;6;5;4;3;2;1', 'failed'
print('passed')

# ------------------------------------------

data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

mysum = 0 

assert mysum == 120, 'failed'
print('passed')


# ------------------------------------------

# Read all users into a list of User objects
# Use data classes
```

## Riesenia

```python
vals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vals2 = [e for nested in vals for e in nested]

assert vals2 == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'failed'
print('passed')
```

```python
data = [1, 2.3, True, 'falcon', 4, -2, False, (1, 2, 3), 9]

data2 = tuple(sorted([e for e in data if type(e) == int]))

assert data2 == (-2, 1, 4, 9), 'failed'
print('passed')
```

```python
data = '1,2,3,4,5,6,7,8,9,10'

data2 = ';'.join(reversed(data.split(',')))

assert data2 == '10;9;8;7;6;5;4;3;2;1', 'failed'
print('passed')
```

```python
def flatten(mylist):
    return [e for nested in mylist for e in nested]


data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

lines = data.splitlines()[1:]
mysum = sum(map(int, flatten(map(lambda e: e.split(','), lines))))

assert mysum == 120, 'failed'
print('passed')
```

```python
@dataclass
class User:
    first_name: str
    last_name: str
    occupation: str


filename = 'users.csv'
users = []

with open(filename, 'r') as f:
    
    for line in f:
        cleaned_line = line.strip()
        fname, lname, occupation  = cleaned_line.split(',')
        user = User(fname, lname, occupation)
        users.append(user)


print(users)
```

## JSON

```python
import requests
import json

url = 'https://webcode.me/users.json'

resp = requests.get(url)
print(resp.status_code)

data = resp.text
print(type(data))

with open('users.json', 'w') as f:

    f.write(data)
```

```python
import requests, json
url = 'https://webcode.me/users.json'

resp = requests.get(url)
print(resp.status_code)

data = resp.json()

with open('users2.json', 'w') as f:

    json.dump(data, f, sort_keys=True, indent=4 * ' ')
```




