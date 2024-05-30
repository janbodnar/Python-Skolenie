# The os module 


## Run an external program

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

### List directory 

The `listdir` function returns a list containing the names of the entries in the directory   
given by path. The list is in arbitrary order, and does not include the special entries  
'.' and '..' even if they are present in the directory. If a file is removed from or added to   
the directory during the call of this function, whether a name for that file be included is unspecified.  

```python
import os 

content = os.listdir('.')
print(content)
```

`scandir` is faster and also provides additional info.   

```python
import os 
from datetime import datetime

path = '.'

with os.scandir(path) as it:
    for entry in it:
        print(f'{entry.name} {datetime.fromtimestamp(entry.stat().st_birthtime)}')
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


## os.path

```python
import os, datetime

path = os.path.join('C://Users/Jano', 'Documents', 'words.txt')
size = os.path.getsize(path)
mtime = os.path.getmtime(path)

print('Size:', size)
print('Last modified:', datetime.datetime.fromtimestamp(mtime))
```
