# Scripts

## count blanks

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
from jinja2 import Environment, FileSystemLoader
import csv
import argparse


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', required=True, help='CSV file name')
    parser.add_argument('-t',  default='Data', help='HTML table title')

    args = parser.parse_args()
    
    return args.f, args.t


def read_data(fname):

    with open(fname, 'r') as f:

        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        data = []
        for row in reader:
            data.append(row)
            
        return headers, data

def write2file(data):

    with open('data.html', 'w') as f:
        f.write(data)


fname, title = parse_args()
headers, rows = read_data(fname)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('data.html')

data = template.render(headers=headers, rows=rows, title=title)
write2file(data)
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


