# Basic standard modules 

Demonstrating some basic standard modules

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

List contents of a ZIP file.  

```python
#!/usr/bin/python


import zipfile

with zipfile.ZipFile('output.zip') as zip:
    print(zip.namelist())
```



