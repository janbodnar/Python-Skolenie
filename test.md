# Priklady


## Lambdas

```python
nums = [1, 2, 3, 4, 5, 6]

print(min(nums))
print(max(nums))


# def get_price(c):
#     return c.price    

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    name: str
    price: int
    production_year: int

cars = [
    Car("Audi", 52642, 2018), Car("Mercedes", 57127, 2019), Car("Skoda", 9000, 2015),
    Car("Volvo", 29000, 2017), Car("Bentley", 350000, 2020), Car("Citroen", 21000, 2016),
    Car("Hummer", 41400, 2014), Car("Volkswagen", 21601, 2013)
]

n = min(cars, key=lambda c: c.production_year)
print(n)

n = max(cars, key=lambda c: c.production_year)
print(n)
```

sorting

```python
#!/usr/bin/python

# cut name into first_name and last_name
users = [
  {'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': 1987},
  {'first_name': 'Jane', 'last_name': 'Doe', 'date_of_birth': 1996},
  {'first_name': 'Robert', 'last_name': 'Brown', 'date_of_birth': 1977},
  {'first_name': 'Lucia', 'last_name': 'Smith', 'date_of_birth': 2002},
  {'first_name': 'Patrick', 'last_name': 'Dempsey', 'date_of_birth': 1994}
]

users.sort(reverse=False, key=lambda user: user['last_name'])

for user in users:
    print(user)
```

## Sum of CSV data


```python
data = '1,2,3,4,5,6,7,8,9,10'

# parts = data.split(',')
# print(parts)

# nums = [int(part) for part in parts]

# print(sum(nums))

print(sum(int(e) for e in data.split(',')))
```



## Fetch web page


```python
import requests

def fetch_homepage():
    """
    Fetches the homepage of https://something.com
    """
    url = "https://something.com"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print("\nPage Content:")
        print(response.text)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
        return None

if __name__ == "__main__":
    fetch_homepage()
```


## Bar chart

```python
import matplotlib.pyplot as plt

# Simple dataset
categories = ['Apple', 'Banana', 'Cherry', 'Date']
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')

# Save the chart as PNG
plt.savefig('bar_chart.png')

print("Bar chart saved as bar_chart.png")
```


## OPenRouter test file

```python
from openai import OpenAI
import os


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# First API call with reasoning
response = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

print("Final response:", response2.choices[0].message.content)
```

## Calculate total sales

```python
import re

text = """
Name      | price  | stock |
Product A |      3 | 2312  |
Product B |     12 | 120   |
Procuct C |     21 | 3450  |
Product D |     11 | 12300 |
"""


pattern = re.compile(r'\d+')

found = re.findall(pattern, text)
print(found)
```

```python
import funcy
import re

text = """
Name      | price  | stock |
Product A |      3 | 2312  |
Product B |     12 | 120   |
Procuct C |     21 | 3450  |
Product D |     11 | 12300 |
"""


pattern = re.compile(r'\d+')

found = re.findall(pattern, text)

vals = [int(val) for val in found]
print(vals)

# Using funcy to pair values
pairs = list(funcy.partition(2, vals))

total = 0
for price, stock in pairs:
    total += price * stock
print(f'Total value of products: {total}')

# n = len(vals) // 2
# products = [vals[i:i + 2] for i in range(0, len(vals), 2)]

# prices = [product[0] for product in products]
# print(prices)
# stocks = [product[1] for product in products]
# print(stocks)

# products = [{'price': price, 'stock': stock} for price, stock in zip(prices, stocks)]
# for i, product in enumerate(products):
#     product['name'] = f'Product {chr(65 + i)}'

# print(products)
```


## Calculate sum

```python
import re

text = """
Product A -> 2312 |
Product B -> 120 |
Procuct C -> 3450 |
Product D -> 12300 |
"""

pattern = re.compile(r'[0-9]+')

found = re.findall(pattern, text)

if found:
    print(f'There are {len(found)} numbers')
    print(found)
```



## Opakovanie

```python
# generate a list of 1000 users with id, first_name, last_name, salary 
# with faker

# read into users of dictionaries list
# extract salaries into salaries list 
# calculate min/max/sum/len/mean/median

# using AI model transform the CSV into SQLite SQL and 
# create a database table

# using Python, read the users from the table into a list 
# and print first 20 and last 20 users.
```




## Opakovanie

`users.csv`

```
Roger,Roe,gardener
Peter,Smith,plumber
Paul,Johnson,teacher
Mary,Johnson,teacher
Carol,Smith,doctor
John,Doe,engineer
Richard,Smith,doctor
Susan,Johnson,teacher
Alex,Johnson,engineer
Roman,Walker,programmer
Alice,Wen,artist
```


```python

# generate a list of 500 random salaries from 850 - 1550 with step 50
# calculate sum, min, max, mean, avg of the salaries

# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

# using a list comprehension, generate a list of random values
# between 1 .. 100. 

# calculate sum using list comprehension
data = "1;2;3;4;5;6,7;8;9;10"

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']


# calculate sum
data = """
1,2,3,4,5
6,7,8,9,10
"""


# read the users.csv file and generate a list of dataclass objects
# filter all teachers from the list


# generate a CSV file with faker, with 1250 rows, with these 
# columns: id, first_name, last_name, email, salary
```




`words.txt`


```
sky
blue
dog
spy
Spy
corridor
prime
PRIME
SNOW
cold
warm
RISK
war
WAR
cup
CUP
```



## Opakovanie

```python
# generate a list of cubes
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter all numbers
data = ['test', 3.0, 5, True, (1, 2), 3.14, None, {'us': 'United States'}, 
        [1, 2, 3], 'hello', 42]

# clean the words, remove leading and trailing spaces, and filter out empty strings
words = [' blue', '\nred', '',  'green', '\t\tyellow', 'purple\n', 
         'sky', 'pawn', 'rock\n', '  ', 'paper', '\t\tscissors']

# using list comprehension, generate a list of random numbers 
# from 1, 100 
# print first 10 and last 10 numbers

# calculate the sum of all numbers in the list
data2 = '1,2,3,4,5,6,7,8,9,10'

# filter users youger than 30 years old
# filter users with last name starting with 'W'
from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'age', 'email'])

users = [
    User('John', 'Doe', 34, 'john.doe@example.com'),
    User('Jane', 'Smith', 28, 'jane.smith@example.com'),
    User('Alice', 'Johnson', 45, 'alice.johnson@example.com'),
    User('Bob', 'Brown', 50, 'bob.brown@example.com'),
    User('Charlie', 'Davis', 22, 'charlie.davis@example.com'),
    User('Emily', 'Wilson', 30, 'emily.wilson@example.com'),
    User('Frank', 'White', 27, 'frank.white@example.com'),
    User('Grace', 'Hall', 38, 'grace.hall@example.com'),
    User('Henry', 'Lewis', 29, 'henry.lewis@example.com'),
    User('Ivy', 'Young', 40, 'ivy.young@example.com'),
    User('Jack', 'Martin', 33, 'jack.martin@example.com'),
    User('Karen', 'King', 26, 'karen.king@example.com'),
    User('Leo', 'Scott', 35, 'leo.scott@example.com'),
    User('Mia', 'Turner', 24, 'mia.turner@example.com'),
    User('Nathan', 'Adams', 37, 'nathan.adams@example.com'),
    User('Olivia', 'Baker', 31, 'olivia.baker@example.com'),
    User('Paul', 'Carter', 42, 'paul.carter@example.com'),
    User('Quinn', 'Flores', 23, 'quinn.flores@example.com'),
    User('Ryan', 'Hill', 48, 'ryan.hill@example.com'),
    User('Sophia', 'Reed', 29, 'sophia.reed@example.com')
]
```



















## Opakovanie

`words.txt`

```
sky
blue
dog
spy
corridor
prime
snow
cold
warm
risk
war
```


```python
# print message using fstring
first_name = 'Roger'
last_name = 'Roe'
occupation = 'gardener'

# create new tuple with elements doubled
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# compute the sum of these values
data = '1,2,3,4,5,6,7,8,9,10'

# filter words starting with 'w'
words = ['sky', 'word', 'worm', 'car', 'type', 
         'car', 'water', 'world']


# create a list of 100 random values
rvals = []

# read words.txt file and print all that 
# start either with 'w' or 'c'
```

## riesenia

```python
# print message using fstring
first_name = 'Roger'
last_name = 'Roe'
occupation = 'gardener'

print(f'{first_name} {last_name} is a {occupation}.')


# create new tuple with elements doubled
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

vals_doubled = []

for val in vals:
    vals_doubled.append(val * 2)

vals_doubled_tuple = tuple(vals_doubled)
print(vals_doubled_tuple)

vals2 = tuple(map(lambda x: x * 2, vals))
print(vals2)

# compute the sum of these values
data = "1,2,3,4,5,6,7,8,9,10"

vals = []

fields = data.split(",")
print(fields)

for e in fields:
    vals.append(int(e))

print(vals)
print(sum(vals))

# print(sum(map(lambda e: int(e), fields)))
print(sum(map(int, fields)))


# filter words starting with 'w'
words = ["sky", "word", "worm", "car", "type", "car", "water", "world"]

words_w = list(filter(lambda word: word[0] == 'w', words))
print(words_w)

words_w = list(filter(lambda word: word.startswith('w'), words))
print(words_w)


words_w_c = list(filter(lambda word: word[0] == 'w' or word[0] == 'c', words))
print(words_w_c)

words_w_c = list(filter(lambda word: word[0] in ('w', 'c'), words))
print(words_w_c)

words_w_c = list(filter(lambda word: word.startswith(('w', 'c')), words))
print(words_w_c)

import random

# create a list of 100 random values, in ranage 1 - 100
rvals = []

for i in range(100):
    rvals.append(random.randint(1, 100))

print(rvals)

file_name = 'words.txt'

with open(file_name, 'r') as fd:
    
    lines = fd.readlines()
    print(lines)
    print(type(lines))

    for line in lines:
        print(line.strip())


    cleaned_lines = list(map(lambda line: line.strip(), lines))
    print(cleaned_lines)

    words_w_c = list(filter(lambda word: word.startswith(('w', 'c')), cleaned_lines))
    print(words_w_c)
```





## Funcy

```python
import funcy

# Sample list of values
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Split into even and odd numbers
evens, odds = funcy.split(lambda x: x % 2 == 0, vals)

print(list(evens))
print(list(odds))
```




```sql
-- Create the 'people' table
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    occupation TEXT
);

-- Insert data into the table
INSERT INTO people (first_name, last_name, occupation) VALUES 
    ('John', 'Doe', 'gardener'),
    ('Roger', 'Doe', 'driver'),
    ('Adam', 'Novak', 'teacher'),
    ('Paul', 'Novak', 'programmer'),
    ('Roman', 'Meszaros', 'programmer'),
    ('Tomas', 'Bruzik', 'driver'),
    ('Lucia', 'Smith', 'teacher'),
    ('Jane', 'Smith', 'teacher');
```






## Functional programming

```python
# def twice(e):
#     return e * 2


vals = [1, 2, 3, 4, 5]

# vals_2 = list(map(twice, vals))
vals_2 = list(map(lambda e: e * 2, vals))

print(vals)
print(vals_2)

vals_3 = [val * 2 for val in vals]
print(vals_3)
```

```python
words = ['hello', 'one', 'world', 'python', 'rocks', 'sky', 'cupcake']

words_3c = list(filter(lambda e: len(e) == 3, words))
print(words_3c)
words_3c = [word for word in words if len(word) == 3]
print(words_3c)
```

procedural style:

```python
words_3c = []

for word in words:
    if len(word) == 3:
        words_3c.append(word)

print(words_3c)
```




```
id,first_name,last_name,occupation,salary
1,Ashley,Curtis,International aid/development worker,6300
2,Christine,Bowman,Immunologist,4200
3,Juan,Howe,Holiday representative,3700
4,Craig,Jordan,Television floor manager,3200
5,Roy,Allen,Engineering geologist,6700
6,Shelly,Rodriguez,Art gallery manager,1100
7,Latoya,Cameron,Geographical information systems officer,6300
8,Renee,Thompson,"Designer, blown glass/stained glass",6800
9,Steven,Mcmillan,Pathologist,6200
10,Jasmine,Holland,"Teacher, adult education",2200
11,Tracy,Wagner,"Solicitor, Scotland",7800
12,Bonnie,Harvey,Systems developer,2600
13,Michael,Roberts,Hydrogeologist,3400
14,Susan,Vaughn,Data processing manager,3300
15,Jessica,Miller,"Designer, exhibition/display",1200
16,Ryan,Jimenez,Chartered accountant,7300
17,Alex,Martinez,"Nurse, children's",4300
18,John,Simmons,"Scientist, audiological",7200
19,Samuel,Francis,Oncologist,1600
20,Eric,Hicks,Podiatrist,3300
21,Billy,Santos,Medical laboratory scientific officer,2800
22,Grant,Johnson,Occupational therapist,4100
23,Stephen,Jimenez,Adult nurse,900
24,Ashley,Garcia,Materials engineer,7700
25,Emily,Brown,"Scientist, research (maths)",6700
26,Catherine,Lopez,Theatre stage manager,1300
27,Jacob,Weeks,"Lecturer, further education",3400
28,Jaime,Smith,Writer,5500
29,Ryan,Hughes,Print production planner,2700
30,Nicole,Graham,Barista,6000
31,Daniel,Galvan,Personal assistant,7500
32,Sarah,Hayes,Advertising account executive,5700
33,Matthew,Hawkins,"Designer, fashion/clothing",2400
34,Bruce,Stewart,Freight forwarder,4700
35,Michele,English,Secretary/administrator,2200
36,Daniel,Martin,Games developer,3600
37,Ashley,Smith,Theme park manager,7200
38,Chris,Gonzalez,Product manager,6600
39,Kristen,Miller,Marine scientist,6800
40,Cindy,Silva,General practice doctor,4300
41,Melissa,Stone,Research scientist (physical sciences),4200
42,Jean,Wilson,Child psychotherapist,7300
43,Marcus,Carlson,Transport planner,6300
44,Scott,Gordon,"Engineer, automotive",3300
45,Susan,Wells,Lobbyist,2800
46,Victoria,French,Operational researcher,7100
47,Joseph,Henry,Farm manager,6500
48,Patrick,Collins,Nature conservation officer,5200
49,Joann,Ross,Research scientist (maths),7200
50,Bob,Romero,Operational researcher,7800
51,Wayne,Marks,Nature conservation officer,4500
52,Lori,Thompson,Environmental consultant,4200
53,Duane,Barber,Veterinary surgeon,4500
54,Emily,Lutz,Field seismologist,4600
55,Theresa,Cook,Psychiatric nurse,2800
56,Danielle,Ramos,Community education officer,4300
57,Kendra,Vazquez,"Merchandiser, retail",4800
58,Christopher,Gordon,"Engineer, broadcasting (operations)",4200
59,Gabriel,Nguyen,Theme park manager,5900
60,Chad,Thompson,"Solicitor, Scotland",3800
61,Kevin,Ramirez,Aeronautical engineer,6300
62,Chad,Bell,"Surveyor, rural practice",3200
63,Tina,Hull,Licensed conveyancer,5500
64,Kristin,Brown,Primary school teacher,1700
65,Stacy,Peterson,"Therapist, speech and language",4900
66,Cheryl,Wu,Homeopath,1400
67,Ernest,Howard,Agricultural consultant,3700
68,Teresa,Andersen,Architectural technologist,6900
69,Amber,Guzman,Haematologist,5100
70,Michelle,Porter,"Therapist, music",3900
71,Douglas,Wood,"Embryologist, clinical",1000
72,Emily,Salazar,Higher education lecturer,6600
73,Daniel,Roberts,Aeronautical engineer,5700
74,Chad,Powell,Phytotherapist,4500
75,Calvin,Roach,"Editor, commissioning",5200
76,Daniel,Rodriguez,Network engineer,2100
77,David,Bradford,Transport planner,4500
78,Stanley,Weber,Rural practice surveyor,5800
79,Whitney,Macias,Landscape architect,4800
80,Deborah,Berry,Theme park manager,5700
81,Debra,Buchanan,Lawyer,6300
82,Eric,Willis,"Psychologist, forensic",5000
83,Mark,Cox,Ecologist,6700
84,Justin,Jones,Television floor manager,1300
85,Christopher,Flores,Financial trader,3200
86,Sarah,Ward,"Accountant, chartered management",3300
87,Jared,Norris,Press sub,5300
88,Blake,Henry,"Programmer, systems",1200
89,Michael,Watkins,Hydrogeologist,4900
90,Charles,Warren,Purchasing manager,1600
91,Madison,Clark,Museum/gallery conservator,2000
92,Lisa,Mullins,Broadcast journalist,5000
93,Erik,Curry,Broadcast journalist,2500
94,Katherine,Cooper,Immunologist,3600
95,Kelly,Gonzalez,Ship broker,5400
96,Kristin,Friedman,Site engineer,4000
97,Dustin,Huynh,Pension scheme manager,2100
98,Jon,Perez,Insurance account manager,3800
99,Anthony,Duncan,Geographical information systems officer,7500
100,John,Andrews,"Clinical scientist, histocompatibility and immunogenetics",3700
```




```sql
CREATE TABLE users(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, occupation TEXT, salary INT);
```



## SQL INJECTION

```python
import sqlite3

name = 'Bratislava'
population = 432000

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()    

    # DO NOT DO THIS, IT IS DANGEROUS, SQL INJECTION
    # print(f"UPDATE cities SET population={population} WHERE name='{name}'")
    # cur.execute(f"UPDATE cities SET population={population} WHERE name='{name}'")
    # cur.execute("UPDATE cities SET population=" + str(population) + " WHERE name= " + name)

    # parameterized query
    cur.execute("UPDATE cities SET population=? WHERE name=?", (population, name))           
    print("Number of rows updated: {}".format(cur.rowcount))
```



## Opakovanie

`users_20.csv`

```
id,first_name,last_name,occupation,salary
1,Ashley,Curtis,International aid/development worker,6300
2,Christine,Bowman,Immunologist,4200
3,Juan,Howe,Holiday representative,3700
4,Craig,Jordan,Television floor manager,3200
5,Roy,Allen,Engineering geologist,6700
6,Shelly,Rodriguez,Art gallery manager,1100
7,Latoya,Cameron,Geographical information systems officer,6300
8,Renee,Thompson,"Designer, blown glass/stained glass",6800
9,Steven,Mcmillan,Pathologist,6200
10,Jasmine,Holland,"Teacher, adult education",2200
11,Tracy,Wagner,"Solicitor, Scotland",7800
12,Bonnie,Harvey,Systems developer,2600
13,Michael,Roberts,Hydrogeologist,3400
14,Susan,Vaughn,Data processing manager,3300
15,Jessica,Miller,"Designer, exhibition/display",1200
16,Ryan,Jimenez,Chartered accountant,7300
17,Alex,Martinez,"Nurse, children's",4300
18,John,Simmons,"Scientist, audiological",7200
19,Samuel,Francis,Oncologist,1600
20,Eric,Hicks,Podiatrist,3300
```


```python
# get status code of https://example.com

import requests
url = "https://example.com"
...

# ==========================================================

# get home page of https://something.com 
# and save it to home.html
import requests
url = "https://something.com"
...

# ==========================================================

prices = [1.5, 2.0, 3.75, 4.25]

total_with_tax = ...  # Add 10% tax to sum of prices

assert total_with_tax == 13.75
print('passed')

# ==========================================================

items = {'apple': 2, 'banana': 3, 'orange': 1}

total_items = ...

assert total_items == 6
print('passed')

# ==========================================================

# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

with open(file_name, 'r') as fd:
    reader = csv.reader(fd)
    ...

# ==========================================================


# print first 5 and last 5 todos from https://jsonplaceholder.typicode.com/todos
import requests

url = "https://jsonplaceholder.typicode.com/todos"
```




## Riesenia

```python
import requests
url = "https://example.com"

resp = requests.get(url)
status_code = resp.status_code
print(status_code)


# get home page of https://something.com 
# and save it to home.html
import requests
url = "https://something.com"

resp = requests.get(url)
file_name = 'home.html'

content = resp.text

with open(file_name, 'w') as fd:
    fd.write(content)

prices = [1.5, 2.0, 3.75, 4.25]


total_with_tax = sum(prices) * 1.1

assert total_with_tax == 12.65
print('passed')



items = {'apple': 2, 'banana': 3, 'orange': 1}

total_items = sum(items.values())

assert total_items == 6
print('passed')



# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

users = []
with open(file_name, 'r') as fd:
    reader = csv.reader(fd)
    
    next(reader)  # skip header

    for row in reader:
        users.append(row)

for users in users[:5]:

    first_name = users[1]
    last_name = users[2]
    job = users[3]
    salary = users[4]
    print(f"{first_name} {last_name} is {job} with salary {salary}")


# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

users = []
with open(file_name, 'r') as fd:
    reader = csv.DictReader(fd)
    
    for row in reader:
        users.append(row)

for users in users[:5]:

    first_name = users['first_name']
    last_name = users['last_name']
    job = users['occupation']
    salary = users['salary']
    print(f"{first_name} {last_name} is {job} with salary {salary}")




# print first 5 and last 5 todos from https://jsonplaceholder.typicode.com/todos
import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
todos = response.json()

print("First 5 todos:")
print(todos[:5])

print("\nLast 5 todos:")
print(todos[-5:])


```















## CSV to JSON

```python
import csv
import json

# Define input and output file names
csv_filename = "test_users.csv"
json_filename = "test_users.json"

# Read CSV and convert to JSON
data = []
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert salary from string to integer
        row["salary"] = int(row["salary"])
        data.append(row)

# Write JSON data to file
with open(json_filename, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"CSV data successfully written to {json_filename}")
```




## process CSV data

```python
import csv
import statistics

file_name = 'test_users.csv'

salaries = []

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)
    
    salaries = [int(row['salary']) for row in reader]

    print(f"Total number of salaries: {len(salaries)}")
    print(f"Minimum salary: {min(salaries)}")
    print(f"Maximum salary: {max(salaries)}")
    print(f"Average salary: {sum(salaries) / len(salaries)}")
    print(f"Median salary: {statistics.median(salaries)}")
```


## generate test CSV data

```python
from faker import Faker
import csv

faker = Faker()

with open('test_users.csv', 'w', newline='') as f:

    fieldnames = ['id', 'first_name', 'last_name', 'occupation', 'salary']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1, 100_000):

        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()
        salary = faker.random_int(min=800, max=8000, step=100)

        writer.writerow({'id': _id, 'first_name': fname, 
            'last_name': lname, 'occupation': occupation, 'salary': salary})
```




## Transform JSON into CSV

```python
import requests
import csv

url = 'https://webcode.me/users.json'

resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()

    print(data)

    file_name = 'users.csv'
    headers = ['id', 'first_name', 'last_name', 'email']
    with open(file_name, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers, lineterminator='\n')

        writer.writeheader()
        for user in data["users"]:
            writer.writerow(user)
```

---

The `users.json` file:

```
{
  "users": [
    {
      "id": 1,
      "first_name": "Robert",
      "last_name": "Schwartz",
      "email": "rob23@gmail.com"
    },
    {
      "id": 2,
      "first_name": "Lucy",
      "last_name": "Ballmer",
      "email": "lucyb56@gmail.com"
    },
    {
      "id": 3,
      "first_name": "Anna",
      "last_name": "Smith",
      "email": "annasmith23@gmail.com"
    },
    {
      "id": 4,
      "first_name": "Robert",
      "last_name": "Brown",
      "email": "bobbrown432@yahoo.com"
    },
    {
      "id": 5,
      "first_name": "Roger",
      "last_name": "Bacon",
      "email": "rogerbacon12@yahoo.com"
    }
  ]
}
```




```python
import csv
import json


def read_json_file(file_name):
    with open(file_name, 'r') as fd:
        data = json.load(fd)
        return data

def write_json_file(file_name, data):

    headers = ['id', 'first_name', 'last_name', 'email']
    with open(file_name, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers, lineterminator='\n')

        writer.writeheader()
        for user in data["users"]:
            writer.writerow(user)


data = read_json_file('users.json')
write_json_file('users.csv', data)
```


## read users.csv file

```python
import csv
import statistics

file_name = "users.csv"

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)

    salaries = []

    for row in reader:

        # print(row)
        print(row['first_name'], row['last_name'], row['salary'])
        salaries.append(int(row['salary']))


    print(salaries)
    print("Average salary: ", statistics.mean(salaries))
    print("Median salary: ", statistics.median(salaries))
```



`users.csv` file

```csv
id,first_name,last_name,salary
1,John,Doe,50000
2,Jane,Smith,60000
3,Bob,Johnson,55000
4,Alice,Williams,70000
5,Charlie,Brown,45000
```




## CSV read file

```python
import csv

file_name = "data.csv"

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    suma = 0
    for row in reader:

        # print(row)

        for field in row:
            suma += int(field)
            
    print(suma)
```



## Retrieve and write HTML page

```python
import requests 

url = 'https://webcode.me/'
resp = requests.get(url)

# print(resp.content.decode('utf-8'))
content = resp.text

with open('home_page.html', 'w') as fd:
    fd.write(content)
```


## Read JSON from URL

```python
import requests

url = "https://webcode.me/users.json"

response = requests.get(url)
data = response.json()

print(data)


for user in data['users']:
    print(f"Name: {user['id']}, First Name: {user['first_name']}, last Name: {user['last_name']}, Email: {user['email']}")

emails = [user['email'] for user in data['users']]

print(emails)
```


## Reading JSON file

```python
import json

fname = 'products.json'
with open(fname) as f:

    data = json.load(f)
    total_sales = 0

    for product in data['products']:
        print(product)

        total_sales = total_sales + float(product['price']) * int(product['quantity'])

    print(f'Total sales: {total_sales}')
```



















```python
import sys
from faker import Faker

filename = sys.argv[1]
n = int(sys.argv[2])

faker = Faker()

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, n+1):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```


```python

import sys

vals = sys.argv[1:]
print(vals)

total = sum(int(val) for val in vals)
print(total)
```



## Generate fake users.csv file

```python

from faker import Faker

faker = Faker()
filename = "users.csv"

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, 100_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```



## Write to file

```python
filename = "words2.txt"

with open(filename, 'w') as fd:

    fd.write('atom\n')
    fd.write('new\n')
    fd.write('small\n')
```


## Append to file

```python

filename = "words2.txt"

with open(filename, 'a') as fd:

    fd.write('cup\n')
    fd.write('cloud\n')
```


## reading files

```python
filename = "words.txt"

with open(filename, 'r') as fd:

    # content = fd.read()
    # print(content.split())

    # lines = fd.readlines()
    # print(lines)

    for line in fd:
        print(line.strip())
```



## dataclasses and namedtuples

```python

from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str
    salary: int


u = User(1, 'Roger', 'Roe', 'driver', 1780)

print(u.last_name)
print(u.salary)

print(u)


# from collections import namedtuple
#
# User = namedtuple('User', 'id first_name last_name occupation salary')
#
# u1 = User(1, "John", "Doe", "gardener", 2300)
# print(u1)
```






## Rectangle

```python
import sys

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height


# print(sys.argv)


width = sys.argv[1]
height = sys.argv[2]


r = Rectangle(int(width), int(height))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



```python
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height

w = input("Enter width:")
h = input("Enter height:")

r = Rectangle(int(w), int(h))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



## Objects

```python


class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 4)
mercy = Cat('Mercy', 1)

print(missy.name, missy.age)
print(lucky.name, lucky.age)
print(mercy.name, mercy.age)

# procedural style:

# cat_name1 = 'Missy'
# cat_age1 = 3
# 
# cat_name2 = 'Lucky'
# cat_age2 = 4
# 
# cat_name3 = 'Mercy'
# cat_age3 = 1
```







The `words.txt` file:

```
smart
war
abyss
ocean
park
water
ram
new
cup
pen
dog
cat
chair
```

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

# using a list comprehension, generate a list of random values
# between 1 .. 100. 

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']

# read words.txt into a list and sort it
```

## Riesenia

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

words2 = [word.lower() for word in words]
print(words2)

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

evens = [val for val in vals if val % 2 == 0]
print(evens)

# using a list comprehension, generate a list of 100 random values
# between 1 .. 100. 
import random

randvals = [random.randint(1, 101) for _ in range(100)]
print(randvals)

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']
# words3 = [word for word in words2 if len(word) == 3 and word.endswith('t')]
words3 = [word for word in words2 if len(word) == 3 and word[-1] == 't']

print(words3)

# read words.txt into a list and sort it
filename = 'words.txt'
with open(filename, 'r') as fd:

    lines = fd.readlines()
    lines_cleaned = [line.strip() for line in lines]

    print(lines_cleaned)

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

data2 = data.replace(',', ';')
print(data2)

fields = data2.split(';')
print(fields)

print(sum(int(field) for field in fields))

# vals = [int(field) for field in fields]
# print(vals)
# 
# print(sum(vals))
```



