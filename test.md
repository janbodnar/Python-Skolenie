# Priklady

## splitlines

```python
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

lines = data.splitlines()
lines.pop(0)

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```

## StringIO

```python
from io import StringIO

# calculate sum
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

# with open('words.txt', 'r') as f:
#    lines = f.readlines()


fdata = StringIO(data)

lines = fdata.readlines()
lines.pop(0)

lines = [line.strip() for line in lines]

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```

## Read CSV from URL using StringIO


```python
import requests
import csv
from io import StringIO
from dataclasses import dataclass


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str


url = 'https://webcode.me/users.csv'

resp = requests.get(url)
content = resp.content.decode('utf8')

users = []

fcsv = StringIO(content)
reader = csv.DictReader(fcsv)

for line in reader:
    u = User(int(line['id']), line['first_name'],
             line['last_name'], line['occupation'])
    # u = User(**line)
    users.append(u)


users_w = [user for user in users if user.last_name.startswith(('W', 'A'))]
print(users_w)
```


