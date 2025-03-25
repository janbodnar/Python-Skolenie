# Priklady

## vypis 11

```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9), (10, 11, 12)))
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




