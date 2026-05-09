# Scripts

## Factorials

```python
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n - 1)


def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial3(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


def factorial4(n):
    from math import factorial

    return factorial(n)


def factorial5(n):
    match n:
        case 0:
            return 1
        case _:
            return n * factorial5(n - 1)


print(factorial1(5))
print(factorial2(5))
print(factorial3(5))
print(factorial4(5))
print(factorial5(5))
```

## Register/login

```python
#!/usr/bin/env python3

import sqlite3
from contextlib import closing

import typer
import bcrypt

DB_NAME = "users.db"

# Pre-computed sentinel used in login to keep timing consistent whether or
# not the username exists, preventing user-enumeration via response time.
_DUMMY_HASH: bytes = bcrypt.hashpw(b"dummy-sentinel", bcrypt.gensalt())

app = typer.Typer(help="Simple user register/login CLI using sqlite and bcrypt")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("""CREATE TABLE IF NOT EXISTS users
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL)""")
    conn.commit()


@app.callback()
def startup() -> None:
    with closing(get_conn()) as conn:
        init_db(conn)


@app.command()
def register(
    username: str | None = typer.Option(
        None, "-u", "--username", help="Username to register"
    )
) -> None:
    """Register a new user. Prompts for username if not provided."""
    if username is None:
        username = typer.prompt("Username")

    password = typer.prompt("Password", hide_input=True, confirmation_prompt=True)

    # bcrypt.hashpw returns bytes; decode for storage
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    with closing(get_conn()) as conn:
        try:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hashed),
            )
            conn.commit()
            typer.secho("Registration successful.", fg=typer.colors.GREEN)
        except sqlite3.IntegrityError:
            typer.secho("Username already exists.", fg=typer.colors.RED)


@app.command()
def list_users() -> None:
    """List all registered users (for demonstration purposes)."""
    with closing(get_conn()) as conn:
        cur = conn.execute("SELECT username FROM users")
        users = cur.fetchall()
        if users:
            typer.secho("Registered users:", fg=typer.colors.GREEN)
            for user in users:
                typer.echo(f"- {user['username']}")
        else:
            typer.secho("No registered users found.", fg=typer.colors.YELLOW)


@app.command()
def login(
    username: str | None = typer.Option(
        None, "-u", "--username", help="Username to login"
    )
) -> None:
    """Login an existing user. Prompts for username if not provided."""
    if username is None:
        username = typer.prompt("Username")

    password = typer.prompt("Password", hide_input=True)

    with closing(get_conn()) as conn:
        cur = conn.execute(
            "SELECT password_hash FROM users WHERE username = ?", (username,)
        )
        row = cur.fetchone()

        stored = row["password_hash"].encode("utf-8") if row else _DUMMY_HASH

        # bcrypt.checkpw expects bytes
        ok = bcrypt.checkpw(password.encode("utf-8"), stored)

        if ok and row:
            typer.secho("Login successful.", fg=typer.colors.GREEN)
        else:
            typer.secho("Invalid username or password.", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
```

The script implements three CLI commands — `register`, `login`, and `list-users` —  
backed by a local SQLite database. Every command that touches the database wraps  
its connection in `contextlib.closing`, which guarantees the connection is  
released even if an exception is raised mid-command. SQLite's own context manager  
only handles transaction boundaries (commit or rollback), so the explicit  
`closing` wrapper is necessary to avoid connection leaks. Database initialisation  
is handled once via Typer's `@app.callback()`, which runs before any sub-command,  
ensuring the `users` table exists without redundantly issuing 
`CREATE TABLE IF NOT EXISTS` on every invocation.  

Password storage is handled correctly. `bcrypt.hashpw` is called with a freshly  
generated salt via `bcrypt.gensalt()`, meaning each registration produces a  
unique digest even if two users choose the same password. The resulting bytes are  
decoded to a UTF-8 string for storage, then re-encoded when retrieved for  
verification. This round-trip is safe because bcrypt digests are ASCII-clean.  
The parameterised query `INSERT INTO users … VALUES (?, ?)` delegates value  
escaping to the SQLite driver, eliminating any SQL injection surface. The  
`UNIQUE` constraint on the `username` column enforces uniqueness at the database  
level, and the `IntegrityError` catch translates that constraint violation into a  
user-facing message without leaking internal details.  

The login flow contains a deliberate defence against timing-based user  
enumeration. If an attacker submits a username that does not exist, a naive  
implementation would return immediately, whereas a successful lookup would spend  
time running `bcrypt.checkpw`. That timing difference is enough to distinguish  
valid from invalid usernames at scale. The fix is to always call `checkpw`  
regardless of whether a row was found. When no row exists, `checkpw` is called  
against `_DUMMY_HASH`, a bcrypt digest computed once at module load time. This  
keeps both code paths at roughly the same cost. The final gate `if ok and row`  
ensures that even if `checkpw` somehow returned `True` against the dummy hash,  
the login would still be rejected because no real row was retrieved.  

One limitation worth noting is that `list-users` exposes all registered usernames  
with no authentication gate, which is acceptable only because the docstring  
explicitly marks it as a demonstration feature. In a production setting this  
command would either be removed or protected.  


## Word count

```python
import re

file_name = 'thermopylae.txt'

pattern = re.compile(r'\w+')

freq = {}
print(type(freq))

with open(file_name, 'r') as file:
    
    content = file.read()

    words = re.findall(pattern, content)
    print(words)

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(freq)

    freq = {}
    # Alternative using get method
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    print(freq)

    # Alternative using setdefault method Note: setdefault returns the value of
    # the key if it is in the dictionary, otherwise it inserts the key with a
    # value of default and returns default.
    for word in words:
        freq[word] = freq.setdefault(word, 0) + 1

    print(freq)

    # Alternative using defaultdict from collections module defaultdict is a
    # subclass of dict that calls a factory function to supply missing values.
    # The default_factory is called without arguments to produce a new value
    # when a key is not found. If default_factory is None, then a KeyError is
    # raised when a missing key is accessed.
    from collections import defaultdict 
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    # Alternative using Counter from collections module
    from collections import Counter
    freq = Counter(words)
    print(freq)
```

## Read CSV file from local server

The CSV file:

```csv
id,first_name,last_name,email,occupation,salary,created_at
1,Jana,Nováková,jana.novakova@example.com,Software Engineer,3200.00,2026-01-01
2,Peter,Kováč,peter.kovac@example.com,Data Analyst,2800.00,2026-01-02
3,Lucia,Horváthová,lucia.horvathova@example.com,Project Manager,3500.00,2026-01-03
4,Martin,Tóth,martin.toth@example.com,UX Designer,3000.00,2026-01-04
5,Simona,Varga,simona.varga@example.com,QA Engineer,2700.00,2026-01-05
6,Marek,Polák,marek.polak@example.com,DevOps Engineer,3400.00,2026-01-06
7,Zuzana,Bartošová,zuzana.bartosova@example.com,HR Specialist,2500.00,2026-01-07
8,Tomáš,Urban,tomas.urban@example.com,Business Analyst,2900.00,2026-01-08
9,Barbora,Králová,barbora.kralova@example.com,Marketing Manager,3300.00,2026-01-09
10,Jozef,Šimek,jozef.simek@example.com,System Administrator,3100.00,2026-01-10
11,Michaela,Dudová,michaela.dudova@example.com,Content Writer,2200.00,2026-01-11
12,Richard,Bielik,richard.bielik@example.com,Product Owner,3600.00,2026-01-12
13,Katarína,Farkašová,katarina.farkasova@example.com,Accountant,2600.00,2026-01-13
14,Andrej,Gregor,andrej.gregor@example.com,Network Engineer,3200.00,2026-01-14
15,Veronika,Kučerová,veronika.kucerova@example.com,Graphic Designer,2400.00,2026-01-15
16,Patrik,Holub,patrik.holub@example.com,Mobile Developer,3300.00,2026-01-16
17,Eva,Švecová,eva.svecova@example.com,Recruiter,2300.00,2026-01-17
18,Roman,Marek,roman.marek@example.com,Database Administrator,3400.00,2026-01-18
19,Monika,Blažeková,monika.blazekova@example.com,Scrum Master,3100.00,2026-01-19
20,Filip,Klein,filip.klein@example.com,Web Developer,3000.00,2026-01-20
```

The server: 

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

CSV_PATH = "users.csv"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(CSV_PATH, "rb") as f:
            data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/csv; charset=utf-8")
        self.send_header("Content-Disposition", "attachment; filename=data.csv")
        self.end_headers()
        self.wfile.write(data)

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
```

The client:


```python
from decimal import Decimal
from io import StringIO
from dataclasses import dataclass

import requests
import csv


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    occupation: str
    salary: Decimal
    created_at: str

    @classmethod
    def from_row(cls, row: dict) -> "User":
        print(cls)
        return cls(
            id=int(row["id"]),
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            occupation=row["occupation"],
            salary=Decimal(row["salary"]),
            created_at=row["created_at"],
        )


response = requests.get("http://localhost:8000/users.csv")
response.encoding = "utf-8"
response.raise_for_status()

users = [User.from_row(row) for row in csv.DictReader(StringIO(response.text))]

for user in users:
    print(user)
```

## Calculate total sales

```python
from functools import reduce
import re

data = """
Name      | Qty | Price  
----------------------
Product A |  12 | $1230 
Product B |  11 | $230 
Product C |   8 | $870 
Product D |   3 | $90 
"""

pattern = re.compile(r'\$(\d{2,4})')

res = re.findall(pattern, data)
prices = [int(e) for e in res]
print(prices)

pattern = re.compile(r'\|\s*(\d+)\s*\|')

res = re.findall(pattern, data)

quantities = [int(e) for e in res]
print(quantities)

total_sales = sum(q * p for q, p in zip(quantities, prices))
print(f"Total Sales: ${total_sales}")

total_sales = reduce(lambda acc, x: acc +
                     x[0] * x[1], zip(quantities, prices), 0)
print(total_sales)
```


## Count blanks

```python
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

fname = args.file

pattern = re.compile(r'\s*$')
blanks = 0
non_blanks = 0

with open(fname, 'r') as r:

    # print(r.readlines())

    for line in r:
        
        if re.fullmatch(pattern, line.strip()):
            blanks += 1
        else:
            non_blanks += 1


print(f'There are {non_blanks + blanks} lines')
print(f'There are {blanks} blank lines')
```

## Read remote CSV file

```python
import requests
from collections import namedtuple

User = namedtuple('User', 'id first_name last_name occupation')

url = 'https://webcode.me/users.csv'

with requests.get(url) as resp:

    content = resp.content.decode('utf8')
    lines = content.splitlines()

    users = []

    for line in lines[1:-1]:
        fields = line.split(',', 3)
        fields_cleaned = [int(fields[0]), fields[1], fields[2], fields[3].replace('"', '')]
        users.append(User(*fields_cleaned))

    print(users[90:101])
```

Using CSV library. 

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
f = StringIO(content)

users = []

for user in csv.DictReader(f):

    u = User(**user)
    users.append(u)
    # print(user)

# for u in users:
#     print(u)

names_w_a = [u for u in users if u.last_name.startswith('W') or u.last_name.startswith('A')]

print(len(names_w_a))

for user in names_w_a:
    print(user)
```


## Top processes by CPU usage

```python
import psutil

processes = [
    {'pid': p.pid, 'name': p.info['name'],
        'sum_cpu_t': sum(p.info['cpu_times'])}
    for p in psutil.process_iter(['name', 'cpu_times'])
]

# sort the processes by the sum of their CPU times (user + system)
sorted_ps = sorted(processes, key=lambda p: p['sum_cpu_t'])

# print the last five
for e in sorted_ps[-5:]:
    print(f'pid: {e['pid']} name: {e['name']} cpu time: {e['sum_cpu_t']}')
```

## Show opened log files 

```python
import psutil

for p in psutil.process_iter(['name', 'open_files']):
    for file in p.info['open_files'] or []:
        if file.path.endswith('.log'):
            print(f"{p.pid:<5} {p.info['name']:<20} {file.path}")
```

## List processes by memory size

```python
import psutil
import argparse

# list processes with memory usage above the 
# given value in MB

parser = argparse.ArgumentParser()
parser.add_argument('memory', help='memory value in MB')

args = parser.parse_args()

mem_limit = int(args.memory) * 1024 * 1024

p_it = psutil.process_iter(['name', 'memory_info'])

large_mem_ps = [{'pid': p.pid, 'name': p.info['name'], 'mem': p.info['memory_info'].rss}
                for p in p_it if p.info['memory_info'].rss > mem_limit]

for p in large_mem_ps:

    print(f'{p['pid']} {p['name']} {(p['mem'] / (1024 * 1024)):.2f}')
```

## List processes

Using `psutil` to list processes and `rich` to format data into console table.  
Currently, rich does not support summary info in the footer.  

The `-a` and `-n` options are mutually exclusive; either we list all processes or  
only a specific process.  

If we provide both short and long options, such as `-a` and `-all`, the parser stores  
the name of the long option.    

```python
import psutil
import argparse
from datetime import datetime
from rich import box
from rich.console import Console
from rich.table import Table
from datetime import date


def parse_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--all', action='store_true',
                       help='show all processes')
    group.add_argument('-n', '--name', help='show info about process name')
    args = parser.parse_args()
    return args.all, args.name


def list_process(name):
    now = f'{date.today()}'
    table = Table(title=f'Process', box=box.MINIMAL,
                  caption=now, caption_justify='left')
    table.add_column('id', style='cyan')
    table.add_column('process name', style='grey69')
    table.add_column('username')
    table.add_column('create time', style='blue')
    table.add_column('memory', style='green')

    process_count = 0

    for p in psutil.process_iter():

        if name in p.name().lower():
            ctime = datetime.fromtimestamp(p.create_time())
            memory_percent = p.memory_percent()
            table.add_row(f'{p.pid}', p.name(), p.username(),
                          ctime.isoformat(), f'{memory_percent:.2f}')
            process_count += 1

    if process_count > 0:

        console = Console()
        console.print(table, justify='center')
    else:

        print('no such process found')


def list_all_processes():

    now = f'{date.today()}'
    table = Table(title='Processes', box=box.MINIMAL,
                  caption=now, caption_justify='left')
    table.add_column('id', style='cyan')
    table.add_column('process name', style='grey69')

    pnames = []
    for p in psutil.process_iter():
        
        pnames.append(p.name())
        table.add_row(f'[bold]{p.pid}', f'[bold]{p.name()}')

    console = Console()
    console.print(table, justify='center')

    print(len(pnames), 'processes')
    print(len(set(pnames)), 'apps')


all_f, name = parse_arguments()

if all_f:
    list_all_processes()
elif name:
    list_process(name)
```


## Resize images

```python

import argparse
import pathlib
from PIL import Image
import os, re

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', default='images', help='source directory')
    parser.add_argument('-d', default='resized_images', help='destination directory')

    args = parser.parse_args()

    return args.s, args.d

def create_dest_dir(dir_name):

    path = pathlib.Path(dir_name)

    if not path.exists():
        path.mkdir()
        
    return path

def get_image_names(dir_name):

    path = pathlib.Path(dir_name)
    file_names = path.glob('*')

    pattern = re.compile(r'.*\.(jpg|jpeg|png)')
    return [fname for fname in file_names if re.fullmatch(pattern, fname.as_posix())] 

def resize_images(path, names):

    for name in names:
        img = Image.open(name).copy()
        img.thumbnail((400, 300))
        img.save(path / os.path.basename(name))

src_dir, dest_dir = parse_args() 

image_fnames = get_image_names(src_dir)
path = create_dest_dir(dest_dir)
resize_images(path, image_fnames)
```

## Count terms 

```python

import httpx
import asyncio
import re


async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = ['https://www.sme.sk', 'https://www.pravda.sk', 'https://www.hlavnespravy.sk',
        'https://hnonline.sk', 'https://www.aktuality.sk',
        'https://dennikn.sk', 'https://www.cas.sk', 'https://www1.pluska.sk']

topics = [{'term': 'Fico', 'pattern': r'Fica|Fico|Ficovi|Ficom', 'count': 0},
          {'term': 'Putin', 'pattern': r'Putin|Putina|Putinovi|Putinom', 'count': 0},
          {'term': 'Trump', 'pattern': r'Trump|Trumpa|Trumpovi|Trumpom', 'count': 0},
          {'term': 'Biden', 'pattern': r'Biden|Biden|Bidenovi|Bidenom', 'count': 0}]


def check_terms(data):

    for html in data:

        for topic in topics:
            pattern = re.compile(topic['pattern'])
            found = re.findall(pattern, html)
            if len(found) > 0:
                topic['count'] += len(found)


async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.content.decode('utf8') for resp in resps]
    check_terms(data)

    for topic in topics:
        print(topic['term'], topic['count'])

asyncio.run(launch())
```

## CSV to HTML

```jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
</head>
<body>

    <h2>{{title}}</h2>

    <table>
        <thead>
        <tr>
            {% for header in headers -%}
            <td>{{ header }}</td>
            {% endfor -%}
        </tr>  
        </thead>

        <tbody>
        {% for row in rows %}
            <tr>
            {% for header in headers -%}
                <td>{{ row[header] -}}</td>
            {% endfor %}
            </tr>
        {% endfor %}
        </tbody>
    </table>

</body>
</html>
```

```python
#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader
import csv
import argparse


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', required=True, help='CSV file name')
    parser.add_argument('-o', default='data.html', help='HTML output file name')
    parser.add_argument('-t', default='Data', help='HTML table title')

    args = parser.parse_args()

    return args.f, args.t, args.o


def read_data(fname):

    with open(fname, 'r') as f:

        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        data = []
        for row in reader:
            data.append(row)
            
        return headers, data

def write2file(data, fname):

    with open(fname, 'w') as f:
        f.write(data)


fname, title, ofname = parse_args()
headers, rows = read_data(fname)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('data.html')

data = template.render(headers=headers, rows=rows, title=title)
write2file(data, ofname)
```

## find/zip files 

```python
import pathlib
import argparse
import zipfile
import tempfile
import time


parser = argparse.ArgumentParser()
   
parser.add_argument('-p', action='store_true', help='print files')
parser.add_argument('-t', required=True, help='file type')
parser.add_argument('-d', help='search directory')
parser.add_argument('-z', action='store_true', help='archive files')
args = parser.parse_args()

p = args.p
z = args.z
file_type = args.t
search_dir = args.d

if not search_dir:
    path = pathlib.Path.home() / 'Documents'
else:
    path = pathlib.Path(search_dir)


n_of_files = 0
archive_files = []

print(f'searching for {file_type} files in {path}')

for fname in path.rglob(f'*.{file_type}'):

    if fname.is_dir():
        continue

    n_of_files += 1

    if z:
        archive_files.append(fname)

    if p:
        print(fname)


print(f'there are {n_of_files} {file_type} files in {path}')


if z:
    time_stamp = str(int(time.time()))
    temp_path = pathlib.Path(tempfile.gettempdir()) / f'archive-{file_type}-{time_stamp}.zip' 

    with zipfile.ZipFile(temp_path, 'w') as zip:

        for fname in archive_files:
            zip.write(fname)

        print(f'{temp_path} created')
```

## find large files 

The `try/except` is used within the for loop in order not to terminate the script  
when we cannot access the file.  

```python
import pathlib
import argparse


def process_args():

    gigabyte = 1024*1024*1024

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', action='store_true', help='print files')
    parser.add_argument('-s', type=int, default=gigabyte,  help='file size in bytes')
    parser.add_argument('-d', help='search directory')

    args = parser.parse_args()
    search_dir = args.d

    if not search_dir:
        path = pathlib.Path.home() / 'Documents'
    else:
        path = pathlib.Path(search_dir)

    return path, args.p, args.s


def should_skip(fname):

    excludes = ['CanonicalGroupLimited']

    for exclude in excludes:
        if exclude in fname.absolute().as_posix():
             return True 
        
    return False


def search_for_large_files(should_print, fsize_limit):

    n_of_files = 0

    for fname in path.rglob('*'):

        if should_skip(fname):
            continue

        try: 
            if fname.is_file():

                fsize = fname.stat().st_size

                if fsize >= fsize_limit:
                    n_of_files += 1

                    if should_print:
                        print(f'{fname} has {fsize:,} bytes')

        except OSError as e:
                print(e)

    return n_of_files


path, should_print, fsize_limit = process_args()
print(f'searching for files larger than {fsize_limit} bytes in {path}')

n_of_files = search_for_large_files(should_print, fsize_limit)
print(f'there are {n_of_files} files larger than {fsize_limit} in {path}')
```

The `stat` and `is_file` or `is_dir` methods are problematic in that they can  
throw exception if they cannot access the file. For instance, the method cannot  
follow a symlink or cannot access the due to permissions.  

```python
def should_skip(fname):

    excludes = ['CanonicalGroupLimited']

    for exclude in excludes:
        if exclude in fname.absolute().as_posix():
             return True 
        
    return False
```

We put the directories that we cannot access into the excludes list and do not  
process them.  



## Deal cards

```python
import random
from collections import namedtuple

n = 6
burns = []
ccards = []

signs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
symbols = ['♣', '♦', '♥', '♠']

cards = [f'{sy}{si}' for si in signs for sy in symbols]
Player = namedtuple('Player', 'name hand')


def shuffle_deal(cards):

    players = []

    random.shuffle(cards)
    deals = [[] for _ in range(n)]

    for _ in range(2):
        for i in range(n):
            deals[i].append(cards.pop())

    for idx, deal in enumerate(deals):
        players.append(Player(f'player {idx+1}', tuple(deal)))

    return players

def deal_community_cards(cards):

    burns.append(cards.pop())

    # flop
    ccards.append(cards.pop())
    ccards.append(cards.pop())
    ccards.append(cards.pop())

    # turn
    burns.append(cards.pop())
    ccards.append(cards.pop())

    # river
    burns.append(cards.pop())
    ccards.append(cards.pop())

    return burns, ccards


players = shuffle_deal(cards)
burns, ccards = deal_community_cards(cards)

print('community cards:', ' '.join(ccards))

print('players')
for p in players:
    print(f'{p.name} has {p.hand}')
```

## Group poker cards by suit

```python
import random
from itertools import groupby

def create_deck():

    signs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    symbols = ['♠', '♥', '♦', '♣']  # spades, hearts, diamonds, clubs

    deck = [f'{si}{sy}' for si in signs for sy in symbols]

    return deck


def by_poker_order(card):

    poker_order = "2 3 4 5 6 7 8 9 10 J Q K A"

    return poker_order.index(card[:-1])


# def by_poker_order2(card):

#     deck = create_deck()

#     return deck.index(card)


deck = create_deck()

# print(deck)
# random.shuffle(deck)
# print(deck)

# Sort by poker order and then by suit
deck.sort(key=by_poker_order)
deck.sort(key=lambda c: c[-1])

# print(deck)

for k, g in groupby(deck, key=lambda c: c[-1]):
    print(k, list(g))
```

## Rank hands

```python
from itertools import combinations
from collections import Counter


def create_deck():

    signs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    symbols = ['♠', '♥', '♦', '♣']  # spades, hearts, diamonds, clubs

    deck = [f'{si}{sy}' for si in signs for sy in symbols]

    return deck


def by_poker_order(card):

    poker_order = "2 3 4 5 6 7 8 9 10 J Q K A"

    return poker_order.index(card[:-1])


def calculate_combinations(hole: list, ccards: list):

    hands = hole + ccards
    hands.sort(key=by_poker_order)

    combs = combinations(hands, 5)
    return tuple(combs)


def check_rank(hole: list, ccards: list):

    combs = calculate_combinations(hole, ccards)

    match is_royal(combs):
        case (True, form):
            print(f'{form} is a royal flush')
            return

    match is_4_kind(combs):
        case (True, form):
            print(f'{form} is four of a kind')
            return

    match is_full_house(combs):
        case (True, form):
            print(f'{form} is a full house')
            return

    match is_flush(combs):
        case (True, form):
            print(f'{form} is a flush')
            return

    match is_3_kind(combs):
        case (True, form):
            print(f'{form} is three of a kind')
            return

    match is_straight(combs):
        case (True, form):
            print(f'{form} is a straight')
            return

    match is_two_pairs(combs):
        case (True, form):
            print(f'{form} is two pairs')
            return

    match is_pair(combs):
        case (True, form):
            print(f'{form} is a pair')
            return

    match is_high_card(combs):
        case (True, form):
            print(f'{form} is a high card')
            return


def is_royal(combs: list):

    royals = ["10♠ J♠ Q♠ K♠ A♠", "10♣ J♣ Q♣ K♣ A♣",
              "10♥ J♥ Q♥ K♥ A♥", "10♦ J♦ Q♦ K♦ A♦"]

    for comb in combs:

        form = ' '.join(comb)

        if form in royals:
            return True, form


def is_4_kind(combs: list):

    four_kinds = []

    for comb in combs:

        c = Counter([e[:-1] for e in comb])
        vals = c.values()

        if 4 in vals:
            form = ' '.join(comb)
            four_kinds.append(form)

    if len(four_kinds) > 0:
        return True, four_kinds[-1]


def is_full_house(combs: list):

    for comb in combs:

        c = Counter([e[:-1] for e in comb])

        vals = c.values()
        form = ' '.join(comb)

        if 2 in vals and 3 in vals:
            return True, form


def is_flush(combs: list):

    matches = ['♣ ♣ ♣ ♣ ♣', '♦ ♦ ♦ ♦ ♦', '♥ ♥ ♥ ♥ ♥', '♠ ♠ ♠ ♠ ♠']
    flushes = []  # there may be more flush combinations, we pick the strongest

    for comb in combs:

        psuits = ' '.join(e[-1] for e in comb)

        if psuits in matches:
            form = ' '.join(comb)
            flushes.append(form)

    if len(flushes) > 0:
        return True, flushes[-1]


def is_straight(combs: list):

    order = "2 3 4 5 6 7 8 9 10 J Q K A"
    strainghts = []

    for comb in combs:

        seq = [e[:-1] for e in comb]
        unit = ' '.join(seq)

        if unit in order:
            form = ' '.join(comb)
            strainghts.append(form)

    if len(strainghts) > 0:
        return True, strainghts[-1]


def is_3_kind(combs: list):

    three_kinds = []

    for comb in combs:

        c = Counter([e[:-1] for e in comb])

        vals = c.values()

        if 3 in vals:
            form = ' '.join(comb)
            three_kinds.append(form)

    if len(three_kinds) > 0:
        return True, three_kinds[-1]


def is_two_pairs(combs: list):

    two_pairs = []

    for comb in combs:

        c = Counter([e[:-1] for e in comb])
        vals = list(c.values())

        if vals.count(2) == 2:

            form = ' '.join(comb)
            two_pairs.append(form)

    if len(two_pairs) > 0:
        return True, two_pairs[-1]


def is_pair(combs: list):

    pairs = []

    for comb in combs:

        c = Counter([e[:-1] for e in comb])
        vals = list(c.values())

        if vals.count(2) == 1:

            form = ' '.join(comb)
            pairs.append(form)

    if len(pairs) > 0:
        return True, pairs[-1]


def is_high_card(combs: list):

    high_cards = []

    for comb in combs:

        form = ' '.join(comb)
        high_cards.append(form)

    if len(high_cards) > 0:
        return True, high_cards[-1]


holes = (['K♥', 'A♣'], ['6♥', '4♠'], ['Q♠', 'Q♣'], ['2♠', '4♣'], ['5♠', '3♠'],
         ['J♣', 'Q♣'], ['Q♦', 'K♦'], ['K♠', 'A♠'], ['6♣', '7♣'], ['2♠', '7♦'])

ccards = (['3♦', '6♠', '10♦', 'J♠', '2♣'],
          ['10♠', 'J♠', 'Q♠', '8♣', '6♠'],
          ['9♠', '10♠', 'J♠', '6♦', '4♥'],
          ['9♠', '3♠', '4♦', '5♦', '6♥'],
          ['9♠', '5♦', '6♦', 'J♠', '3♣'],
          ['9♣', '10♣', '2♣', '3♣', '4♥'],
          ['4♦', '7♥', '7♦', 'A♣', '6♠'],
          ['5♦', '6♦', '10♣', '2♦', '2♣'],
          ['5♦', '5♣', '5♥', '6♦', '2♣'],
          ['5♣', '5♥', '6♦', '2♣', '4♦'],
          ['A♣', '10♣', '6♦', '3♦', 'K♣'])

for hole in holes:
    for ccard in ccards:
        check_rank(hole, ccard)
```




