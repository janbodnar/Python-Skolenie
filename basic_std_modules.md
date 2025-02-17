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

## subprocess

```python
import subprocess

def show_edit_environment_variables_dialog():
    try:
        # Command to open the System Properties window
        command = "SystemPropertiesAdvanced"

        # Run the command using subprocess
        subprocess.run(command, shell=True)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    show_edit_environment_variables_dialog()
```


## sys module 

### The executable

```python
import sys

print(sys.executable)
```

### The sys.modules 

The `sys.modules` is a dictionary containing all the modules that have ever been imported since Python was started.  

```python
import sys

print(sys.modules)

for m in sys.modules:
    print(m)

import math, os, random

for m in sys.modules:
    print(m)
```

### Various system information

```python


import sys

print(sys.argv)
print(sys.byteorder)
print(sys.platform)
print(sys.version)
print(sys.version_info)
print(sys.implementation)
print(sys.path)
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

## Using requests

```python
import json
import requests

url = 'http://time.jsontest.com'

resp = requests.get(url)

# text = resp.content.decode("UTF8")
# data = json.loads(text)

data = resp.json()

print(f"Unix time: {data['milliseconds_since_epoch']}")
print(f"Time: {data['time']}")
print(f"Date: {data['date']}")
```

## Using urllib3

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

Create a ZIP file

```python
import zipfile

files_to_zip = ['load_data.py', 'load_data2.py']

with zipfile.ZipFile('pyarchive.zip', 'w') as zip:
    for file in files_to_zip:
        zip.write(file)
```


Extract a ZIP file.  

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

## Append file 

```python
import zipfile

# Open the existing ZIP file in append mode
with zipfile.ZipFile('pyarchive.zip', 'a') as zip:
    # Print the current files in the ZIP
    print("Current files in the ZIP:", zip.namelist())

    # Add a new file to the ZIP
    new_file = 'newfile.txt'
    zip.write(new_file, arcname='newfile.txt')

    # Print the updated list of files in the ZIP
    print("Updated files in the ZIP:", zip.namelist())
```


## Change registry

```python
import winreg as reg
import ctypes
import os

def enable_long_paths():
    try:
        # Open the registry key
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\FileSystem", 0, reg.KEY_SET_VALUE)

        # Set the LongPathsEnabled value to 1
        reg.SetValueEx(key, "LongPathsEnabled", 0, reg.REG_DWORD, 1)

        # Close the registry key
        reg.CloseKey(key)

        # Inform the user
        print("Successfully enabled long paths in the registry.")

        # Check if the script has administrative privileges
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if not is_admin:
            print("Please run this script with administrative privileges for the changes to take effect.")

    except PermissionError:
        print("Error: You need to run this script as an administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    enable_long_paths()
```



