# Basic standard modules 

https://docs.python.org/3/library/index.html

Demonstrating some basic standard modules

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

## Example

Read the contents of the `PATH` variable and find all Python content.  


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



