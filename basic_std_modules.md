# Basic standard modules 

https://docs.python.org/3/library/index.html

Demonstrating some basic standard modules

## Tasks

- Read the contents of the `PATH` variable and find all Python content.  
- Read the contents of the current working directory and print only Python files.
- Read the contents of the current working directory and print first 10 Python files.
- Read webcode.me/words.txt file & print the words in sortet order. Print only words  
  starting in 'w' or 'c'.
- Read JSON data from `https://webcode.me/users.json` and load it into a dictionary.  

## os 

Run an external program

```python
#!/usr/bin/python

import os

os.system('code')
```

## Get current working directory

```python
import os

print(os.getcwd())
```

### Renaming

```python
import os 

oldname = 'words.txt'
newname = 'words2.txt'

os.rename(oldname, newname)
```

### Run and read the output.

```python
#!/usr/bin/python

import os

output = os.popen('dir').read()
print(output)
```

### Read environment variables 

```python
import os 

print(os.name)
print(os.environ['PATH'])
print(os.environ['USERNAME'])
print(os.environ['OS'])
print(os.environ['TMP'])
```

### Make directory

A new directory/folder is created with `mkdir`.  

```python
import os 
import sys

cur_dir = os.getcwd()
new_dir = 'data'
path = f'{cur_dir}/{new_dir}'

if os.path.exists(path):
    print('file/directory already exists')
    sys.exit(1)

os.mkdir(path)

if os.path.exists(path):
    print('file/directory is created')
```

---

Make multiple directories in one shot with `makedirs`.  

```python
import os 
import sys

cur_dir = os.getcwd()
new_dir = 'data/text/2024'
path = f'{cur_dir}/{new_dir}'

if os.path.exists(path):
    print('file/directory already exists')
    sys.exit(1)

os.makedirs(path)

if os.path.exists(path):
    print('file/directory is created')
```

### Walking directories. 

```python
import os

# for root, dirs, files in os.walk("."):
for root, dirs, files in os.walk(os.path.abspath(".")):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
```

### Executing programs

These functions all execute a new program, replacing the current process; they do not return.  

```python
os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)
```

The `e`, `v`, `p`, and `l` letters mean:

- **`l`**: This stands for "list". When this letter is present, it means the function expects  
  the arguments to be passed in as separate parameters (i.e., `arg0`, `arg1`, ...). For example,  
  in `os.execl(path, arg0, arg1, ...)`, `arg0`, `arg1`, etc. are separate arguments.  

- **`v`**: This stands for "vector". When this letter is present, it means the function expects  
  the arguments to be passed in as a list or tuple. For example, in `os.execv(path, args)`, `args`   
  is a list or tuple of arguments.  

- **`e`**: This stands for "environment". When this letter is present, it means the function allows  
  you to modify the environment for the command being run. For example, in `os.execle(path, arg0, arg1, ..., env)`, `env`  
  is a dictionary that contains the environment variables.  

- **`p`**: This stands for "path". When this letter is present, it means the function will use the `PATH`  
  environment variable to find the executable. For example, in `os.execlp(file, arg0, arg1, ...)`, the function  
  will look for `file` in the directories listed in the `PATH` environment variable.  


```python
import os 

name = 'test.py'

command = ["python", "test.py"]
os.execvp(command[0], command)

print('finished') # this line is not reached
```




## Platform 

Get platform information with the `platform` module.  

```python
import platform

plat = platform.system()
print(plat)

arch = platform.architecture()
print(arch)

version = platform.version()
print(version)

py_branch = platform.python_branch()
print(py_branch)

processor = platform.processor()
print(processor)

machine = platform.machine()
print(machine)
```


## json

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format  
that is easy for humans to read and write and easy for machines to parse and  
generate. It is based on a subset of JavaScript Programming Language, Standard  
ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely  
language independent but uses conventions that are familiar to programmers of  
the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python,  
and many others. These properties make JSON an ideal data-interchange language.  

The `json` module in Python provides a method called `json.dumps()` that converts  
a Python object into a JSON string. This module also provides a `json.loads()`  
method that can be used to parse a JSON string and convert it into a Python  
object.  

Write dictionary to JSON file with `dump`. 

```python
#!/usr/bin/python

import json

data = {"name": "Jane", "age": 17}

fname = 'friends.json'
with open(fname, 'w') as f:
    json.dump(data, f)
```

Read JSON from file into dictionary with `load`.

```python
#!/usr/bin/python

import json

fname = 'products.json'
with open(fname) as f:

    data = json.load(f)

    for e in data['products']:
        print(e)
```

Pretty print 

```python
#!/usr/bin/python

import json

json_data = {"name":"Audi", "model":"2012", "price":22000,
                 "colours":["gray", "red", "white"]}

data = json.dumps(json_data, sort_keys=True, indent=4 * ' ')

print(data)
```

Read JSON into dictionary with `loads`. 

```python
#!/usr/bin/python

import json

json_data = '{"name": "Jane", "age": 17}'

data = json.loads(json_data)

print(type(json_data))
print(type(data))

print(data)
```

Read JSON from URL. 

```python
#!/usr/bin/python

import json
import urllib3


http = urllib3.PoolManager()

url = 'http://time.jsontest.com'

resp = http.request('GET', url)
text = resp.data.decode("utf-8")

data = json.loads(text)

print(f"Unix time: {data['milliseconds_since_epoch']}")
print(f"Time: {data['time']}")
print(f"Date: {data['date']}")
```


## urllib3

```python
#!/usr/bin/python

import urllib3


http = urllib3.PoolManager()

url = 'https://webcode.me'

resp = http.request('GET', url)
print(resp.status)
```

GET request 

```python
#!/usr/bin/python

import urllib3


http = urllib3.PoolManager()

url = 'https://webcode.me'

resp = http.request('GET', url)
print(resp.data.decode('utf-8'))
```

HEAD request

```python
#!/usr/bin/python

import urllib3


http = urllib3.PoolManager()

url = 'https://webcode.me'
resp = http.request('HEAD', url)

print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.headers['Content-Type'])
print(resp.headers['Last-Modified'])
```


## secrets 

```python
#!/usr/bin/python


import string
import secrets

chars = string.ascii_letters + string.digits + string.punctuation
passwd = "".join(secrets.choice(chars) for i in range(8))

print(passwd)
```

```python
#!/usr/bin/python


import secrets

with open("unix-words.txt") as f:
    words = [word.strip() for word in f]
    password = " ".join(secrets.choice(words) for i in range(4))
    print(password)
```

Example uses traditional `try/except/finally` keywords. 

```python
#!/usr/bin/python

import secrets

try:
    f = open("unix-words.txt")
    words = [word.strip() for word in f]
    password = " ".join(secrets.choice(words) for i in range(4))
    print(password)
except Exception as e:
    print("An error occurred: ", e)
finally:
    f.close()
```

## zipfile 

Create a ZIP file.  

```python
#!/usr/bin/python

import zipfile

with zipfile.ZipFile('output.zip', 'r') as zip_ref:
    zip_ref.extractall('tmp')
```

Extract a specific file 

```python
#!/usr/bin/python


import zipfile

with zipfile.ZipFile('output.zip') as zip:

    zip.extract('funs.py', '.')
```


List contents of a ZIP file.  

```python
#!/usr/bin/python


import zipfile

with zipfile.ZipFile('output.zip') as zip:
    print(zip.namelist())
```



