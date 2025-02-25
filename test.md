
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




