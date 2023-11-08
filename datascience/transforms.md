# Data transformations

## Generate test data in CSV format

Generating user data with `faker` and `csv` modules.  

```python
#!/usr/bin/python

from faker import Faker
import csv

faker = Faker()

with open('users.csv', 'w', newline='') as f:
    fieldnames = ['id', 'first_name', 'last_name', 'occupation']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1, 101, 1):
        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()

        writer.writerow({'id': _id, 'first_name': fname, 
            'last_name': lname, 'occupation': occupation})
```

## Transform CSV data into XLSX format

Using `csv` and `openpyxl` modules.  

```python
#!/usr/bin/python

from openpyxl import Workbook
import csv

def read_data(data):

    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append((int(row['id']), row['first_name'], 
                row['last_name'], row['occupation']))

data = []

book = Workbook()
sheet = book.active

sheet.append(['Id', 'First name', 'Last name', 'Occupation'])
read_data(data)

for e in data:
    sheet.append(e)

book.save('users.xlsx')
```

## Transform CSV data into JSON

Using `csv` and `json` modules.  

```python
#!/usr/bin/python

from openpyxl import Workbook
import json, csv

def read_data(data):

    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append({'id': row['id'], 'first_name': row['first_name'], 
                'last_name': row['last_name'], 'occupation': row['occupation']})

data = []
read_data(data)

with open('users.json', 'w') as f:
    json.dump(data, f)
```

## Transform CSV data into HTML

Using `csv` and `jinja2` modules.  

```python
#!/usr/bin/python

from openpyxl import Workbook
from jinja2 import Environment, FileSystemLoader
import csv

def read_data(data):

    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append({'id': row['id'], 'first_name': row['first_name'], 
                'last_name': row['last_name'], 'occupation': row['occupation']})

def write2file(data):
    with open('users.html', 'w') as f:
        f.write(data)

users = []
read_data(users)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('users.html')

data = template.render(users=users)
write2file(data)
```

The template.  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users</title>
</head>
<body>

    <h2>Users</h2>

    <table>
        <thead>
        <tr>
            <th>Id</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Occupation</th>
        </tr>
        </thead>

        <tbody>
        {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.first_name }}</td>
                <td>{{ user.last_name }}</td>
                <td>{{ user.occupation }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>

</body>
</html>
```

## CSV and SQLite database

Programatically with `sqlite3` module.  
We can also do it with `sqlite3` tool:  

`CREATE TABLE users2(id INT, first_name TEXT, last_name TEXT, occupation TEXT);`  
`sqlite> .import users.csv users2`  

Export into CSV from SQLite database: `$ sqlite3 -header -csv test.db "select * from users;" > users3.csv`  

```
sqlite> .headers on
sqlite> .mode csv
sqlite> .output users4.csv
sqlite> select * from users;
```

### Load into database

```python
#!/usr/bin/python

import sqlite3
import csv

def read_data(data):

    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append((int(row['id']), row['first_name'], 
                row['last_name'], row['occupation']))


data = []
read_data(data)

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("CREATE TABLE users(id INT, first_name TEXT, last_name TEXT, occupation TEXT)")
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", data)
```

### Fetch from database into CSV 

```python
#!/usr/bin/python

import sqlite3
import csv

def write_data(data):

    with open('users2.csv', 'w', newline='') as f:

        fnames = ['id', 'first_name', 'last_name', 'occupation']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()

        for row in data:
            writer.writerow({'id': row['id'], 'first_name': row['first_name'],
                'last_name': row['last_name'], 'occupation': row['occupation']})

data = []

con = sqlite3.connect('test.db')
with con:

    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    for row in rows:
        data.append({'id': row['id'], 'first_name': row['first_name'],
                'last_name': row['last_name'], 'occupation': row['occupation']})

write_data(data)
```

## Return JSON data from a web application

Return JSON data from a Flask application.  

`flask --app webapp run`  

```python
#!/usr/bin/python

from flask import Flask, make_response

app = Flask(__name__)

@app.route("/users")
def get_users():

    users = load_data()

    resp = make_response(users)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp


def load_data():
    with open('users.json', 'r') as f:
        users = f.read()
        return users
```

## Fetch JSON and transform into CSV

Fetch JSON data from a running Flask application and transform the  
data into CSV format.  

Using `json`, `csv`, and `httpx` modules.  

Generate a HTTP GET request with httpie application.  
`$ http GET http://localhost:5000/users`

```python
#!/usr/bin/python

from openpyxl import Workbook
import json, csv
import httpx


def write_data(data):

    with open('users2.csv', 'w', newline='') as f:

        fnames = ['id', 'first_name', 'last_name', 'occupation']
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()

        for row in data:
            writer.writerow({'id': row['id'], 'first_name': row['first_name'],
                'last_name': row['last_name'], 'occupation': row['occupation']})


r = httpx.get('http://localhost:5000/users')
json_data = r.text

data = json.loads(json_data)
write_data(data)
```

## Output CSV data in console table 

Using `csv` and `rich` modules.  

```python
#!/usr/bin/python

import csv
from rich import box
from rich.console import Console
from rich.table import Table
from datetime import date

now = f'{date.today()}'
table = Table(title='Users', box=box.MINIMAL, caption=now, caption_justify='left')

table.add_column('Id', style='cyan')
table.add_column('First name', style='grey69')
table.add_column('Last name', style='grey69')
table.add_column('Occupation', style='green')

def read_data(data):

    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            data.append({'id': row['id'], 'first_name': row['first_name'], 
                'last_name': row['last_name'], 'occupation': row['occupation']})

data = []
read_data(data)

for row in data:
    table.add_row(row['id'], row['first_name'], row['last_name'], row['occupation'])

console = Console()
console.print(table, justify='center')
```



