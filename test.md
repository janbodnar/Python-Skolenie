# Priklady

## Opakovanie


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

assert number_of_words == 117, 'passed'
print('failed')

# ----------------------------------------------------------


# write script that reads data from 
# https://webcode.me/users.xml, use copilot
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




