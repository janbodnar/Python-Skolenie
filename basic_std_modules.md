# Basic standard modules 

https://docs.python.org/3/library/index.html

Demonstrating some basic standard modules

## Tasks

- Read the contents of the `PATH` variable and find all Python content.  
- Read the contents of the current working directory and print only Python files.
- Read the contents of the current working directory and print first 10 Python files.
- Read webcode.me/words.txt file & print the words in sortet order. Print only words
  starting in 'w' or 'c'.

## os 

Run an external program

```python
#!/usr/bin/python

import os

os.system('code')
```

Run and read the output.

```python
#!/usr/bin/python

import os

output = os.popen('dir').read()
print(output)
```

Read environment variables 

```python
#!/usr/bin/python

import os

print(os.environ)
print(os.getenv("PATH"))
```

Walking directories. 

```python
#!/usr/bin/python


import os

# for root, dirs, files in os.walk("."):
for root, dirs, files in os.walk(os.path.abspath(".")):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
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

Write to file with `dump`. 

```python
#!/usr/bin/python

import json

data = {"name": "Jane", "age": 17}

fname = 'friends.json'
with open(fname, 'w') as f:
    json.dump(data, f)
```

Read from file with `load`.

```python
#!/usr/bin/python

import json

fname = 'products.json'
with open(fname) as f:

    data = json.load(f)

    for e in data['products']:
        print(e)
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



