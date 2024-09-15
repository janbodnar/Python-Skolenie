# Scripts

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
    group.add_argument('-a', '--all', action='store_true', help='show all processes')
    group.add_argument('-n', '--name', help='show info about process name')
    args = parser.parse_args()
    return args.all, args.name

def list_process(name):
    now = f'{date.today()}'
    table = Table(title='Users', box=box.MINIMAL, caption=now, caption_justify='left')
    table.add_column('id', style='cyan')
    table.add_column('process name', style='grey69')
    table.add_column('username')
    table.add_column('create time', style='blue')
    table.add_column('memory', style='green')
    # table.show_footer = True

    total_memory = 0
    process_count = 0

    for p in psutil.process_iter():
        if name in p.name().lower():
            ctime = datetime.fromtimestamp(p.create_time())
            memory_percent = p.memory_percent()
            table.add_row(f'{p.pid}', p.name(), p.username(), ctime.isoformat(), f'{memory_percent:.2f}')
            total_memory += memory_percent
            process_count += 1

    table.add_row(f'[bold]{process_count}', '', '', '', f'[bold]{total_memory:.2f}')

    console = Console()
    console.print(table, justify='center')

def list_all_processes():
    pnames = []
    for p in psutil.process_iter():
        pnames.append(p.name())
        print(f"pid: {p.pid}, name: {p.name()}")
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




