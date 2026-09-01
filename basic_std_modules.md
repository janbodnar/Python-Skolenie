# Basic Standard Modules in Python

Python's standard library is vast and powerful, providing a rich set of modules  
for various tasks. This document explores some of the most commonly used  
standard modules, demonstrating their practical applications.

**Official Documentation:**  
https://docs.python.org/3/library/index.html

---

## Common Tasks with Standard Modules

Throughout this guide, we'll cover these essential tasks:

- Read the `PATH` environment variable and locate all Python-related content  
- List Python files in the current working directory  
- Display only the first 10 Python files from the current directory  
- Fetch and sort words from `webcode.me/words.txt`, filtering words starting  
  with 'w' or 'c'  
- Load JSON data from `https://webcode.me/users.json` into a Python dictionary  

The final section of this document, **"Putting It All Together,"** demonstrates  
all five tasks using the modules we've explored.

---

## The `os` Module

The `os` module provides a portable way of using operating system-dependent  
functionality, including environment variables, file paths, and directory  
operations.

### Working with Environment Variables

```python
import os

# Get a specific environment variable
path_var = os.environ.get("PATH")
print("PATH:", path_var)

# Split PATH into individual directories
path_dirs = path_var.split(os.pathsep)
print("Directories in PATH:", path_dirs)

# Find Python-related entries in PATH
python_paths = [p for p in path_dirs if "python" in p.lower()]
print("Python-related paths:", python_paths)
```

**Explanation:** The `os.environ` dictionary contains all environment variables.  
`os.pathsep` returns the platform-specific path separator (`;` on Windows,  
`:` on Unix). This allows robust parsing of the `PATH` variable across systems.

### Working with Directories

```python
import os

# Get the current working directory
cwd = os.getcwd()
print("Current directory:", cwd)

# List all files in the current directory
all_files = os.listdir()
print("All files:", all_files)

# List only Python files
py_files = [f for f in os.listdir() if f.endswith('.py')]
print("Python files:", py_files)
```

---

## The `pathlib` Module (Modern Alternative)

`pathlib` offers an object-oriented approach to file system paths and is  
considered more modern than `os.path`. It's part of the standard library.

```python
from pathlib import Path

# Get current directory
cwd = Path.cwd()
print("Current directory:", cwd)

# List all Python files
py_files = list(cwd.glob("*.py"))
print("All Python files:", py_files)

# Get first 10 Python files
first_10 = py_files[:10]
for py_file in first_10:
    print(f"File: {py_file}")

# Alternative: use islice for efficient slicing
from itertools import islice
first_10_sliced = list(islice(cwd.glob("*.py"), 10))
```

**Pathlib advantages:**
- More readable, object-oriented syntax  
- Cross-platform path handling without using strings  
- Chainable methods like `.parent`, `.stem`, `.suffix`  

---

## The `itertools` Module

`itertools` provides efficient looping functions, including `islice()` for  
slicing iterators without converting them to lists.

```python
import itertools

# Slice an iterator directly (memory-efficient)
first_10 = list(itertools.islice(Path.cwd().glob("*.py"), 10))
```

**Use case:** When working with large directories or streaming data, `islice`  
prevents loading everything into memory at once.

---

## The `sys` Module

The `sys` module provides access to system-specific parameters and functions,  
including command-line arguments, the Python interpreter path, and more.

### Finding the Python Executable

```python
import sys

print(sys.executable)
```

**Output:** `/usr/bin/python3` or a similar path showing where Python is installed.

### Working with Imported Modules

```python
import sys

# Display all modules loaded so far
print(sys.modules)

# Iterate through module names
for m in sys.modules:
    print(m)

# Import additional modules
import math, os, random

for m in sys.modules:
    print(m)
```

The `sys.modules` dictionary contains all modules that have been imported  
since the Python interpreter started. It's useful for debugging and  
understanding what's loaded in memory.

### System Information

```python
import sys

print(sys.argv)          # Command-line arguments
print(sys.byteorder)     # Byte order of the system ('little' or 'big')
print(sys.platform)      # Platform identifier
print(sys.version)       # Python version string
print(sys.version_info)  # Version as a tuple
print(sys.implementation)# Python implementation details
print(sys.path)          # Module search path
```

**Output Examples:**
- `sys.argv`: List of command-line arguments passed to the script  
- `sys.byteorder`: `'little'` on most modern systems  
- `sys.platform`: `'win32'`, `'linux'`, or `'darwin'` (macOS)  
- `sys.path`: List of directories where Python looks for modules  

---

## The `platform` Module

The `platform` module provides detailed platform identification information,  
making it easy to write cross-platform code.

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

**Sample Output:**
```
Windows
('64bit', 'WindowsPE')
10.0.19045
main
Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
AMD64
```

**Common Uses:**
- Conditional code based on OS: `if platform.system() == "Windows":`  
- Determining whether code is running on 32-bit or 64-bit architecture  

---

## The `json` Module

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format  
that is easy for humans to read and write, and easy for machines to parse and  
generate. Python's `json` module provides full support for JSON operations.

### Writing JSON to a File

```python
import json

data = {"name": "Jane", "age": 17}

fname = 'friends.json'
with open(fname, 'w') as f:
    json.dump(data, f)
```

**Explanation:** The `json.dump()` function serializes a Python object and  
writes it directly to a file. The `with` statement ensures the file is  
properly closed after writing.

### Reading JSON from a File

```python
import json

fname = 'products.json'
with open(fname) as f:
    data = json.load(f)
    for e in data['products']:
        print(e)
```

The `json.load()` function reads a JSON file and converts it to a Python  
object (typically a dictionary or list).

### Pretty Printing JSON

```python
import json

json_data = {"name":"Audi", "model":"2012", "price":22000,
             "colours":["gray", "red", "white"]}

data = json.dumps(json_data, sort_keys=True, indent=4 * ' ')

print(data)
```

**Output:**
```json
{
    "colours": [
        "gray",
        "red",
        "white"
    ],
    "model": "2012",
    "name": "Audi",
    "price": 22000
}
```

**Parameters explained:**
- `sort_keys=True`: Sorts dictionary keys alphabetically  
- `indent=4 * ' '`: Uses 4 spaces for indentation  

### Converting JSON Strings to Python Objects

```python
import json

json_data = '{"name": "Jane", "age": 17}'

data = json.loads(json_data)

print(type(json_data))  # <class 'str'>
print(type(data))       # <class 'dict'>
print(data)             # {'name': 'Jane', 'age': 17}
```

The `json.loads()` function parses a JSON string and returns a Python object.

### Fetching JSON from a URL Using `requests`

The `requests` library (available via `pip install requests`) simplifies HTTP  
requests. This is a **third-party package**, not part of the standard library,  
but worth covering due to its widespread use.

```python
import json
import requests

url = 'http://api.open-notify.org/iss-now.json'

resp = requests.get(url)
data = resp.json()  # Directly parse JSON response

print(data)
print(data['timestamp'])
print(data['iss_position'])
print(data['message'])
```

**Key features of `requests`:**
- Automatic JSON parsing with `.json()` method  
- Handles HTTP errors gracefully  
- Supports all HTTP methods (GET, POST, PUT, DELETE)  

### Fetching JSON Using Standard `urllib` (Standard Library)

```python
import json
import urllib.request

url = 'http://time.jsontest.com'

with urllib.request.urlopen(url) as response:
    text = response.read().decode("utf-8")
    data = json.loads(text)

print(f"Unix time: {data['milliseconds_since_epoch']}")
print(f"Time: {data['time']}")
print(f"Date: {data['date']}")
```

**Explanation:** This uses the standard library's `urllib.request` module,  
which is available without installing additional packages. The `urlopen()`  
function returns a file-like object that can be read and decoded.

---

## The `urllib` Module for HTTP Requests (Standard Library)

The `urllib` module is included in Python's standard library and provides  
HTTP request functionality without external dependencies.

### Basic GET Request

```python
import urllib.request

url = 'https://webcode.me'

with urllib.request.urlopen(url) as response:
    print(response.status)  # HTTP status code
    html = response.read().decode('utf-8')
    print(html[:200])       # First 200 characters
```

### HEAD Request Using `urllib`

```python
import urllib.request

url = 'https://webcode.me'

# Create a request object and get headers
req = urllib.request.Request(url, method='HEAD')
with urllib.request.urlopen(req) as response:
    print(response.headers['Server'])
    print(response.headers['Date'])
    print(response.headers['Content-Type'])
    print(response.headers['Last-Modified'])
```

**Output:**
```
nginx
Wed, 01 Sep 2026 10:30:00 GMT
text/html
Tue, 31 Aug 2026 08:30:00 GMT
```

A HEAD request retrieves only the headers, not the body, making it useful for  
checking metadata without downloading large content.

### Important Note: `urllib3` vs `urllib`

**Correction:** The `urllib3` module mentioned in earlier examples is **not**  
part of the Python standard library. It's a third-party package (a dependency  
of `requests`, actually). The standard library's HTTP module is `urllib`  
(with submodules `urllib.request`, `urllib.parse`, etc.). Use `urllib` for  
standard library examples.

---

## The `secrets` Module

The `secrets` module is used for generating cryptographically strong random  
numbers suitable for managing secrets like passwords, account authentication,  
tokens, and similar.

### Generating a Random Password

```python
import string
import secrets

chars = string.ascii_letters + string.digits + string.punctuation
passwd = "".join(secrets.choice(chars) for i in range(8))

print(passwd)
```

**Explanation:**  
- `string.ascii_letters`: All ASCII letters (a-z, A-Z)  
- `string.digits`: Digits 0-9  
- `string.punctuation`: Special characters like !@#$%^&*  
- `secrets.choice()`: Selects a random character from the sequence  
- The `join()` creates a string of 8 random characters  

### Generating a Passphrase from a Word List

```python
import secrets

# Using 'with' ensures the file is properly closed
with open("unix-words.txt") as f:
    words = [word.strip() for word in f]
    password = " ".join(secrets.choice(words) for i in range(4))
    print(password)
```

**Example output:** `"azure elephant quantum melody"`

This approach creates memorable yet secure passwords using randomly selected  
words from a dictionary.

### Combining `with` and Exception Handling

```python
import secrets

try:
    with open("unix-words.txt") as f:
        words = [word.strip() for word in f]
        password = " ".join(secrets.choice(words) for i in range(4))
        print(password)
except FileNotFoundError:
    print("Error: The word list file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Best Practice:** The `with` statement automatically handles resource cleanup  
(file closing), while `try/except` manages potential errors. This is cleaner  
and safer than using `try/except/finally` with manual `.close()` calls.

---

## The `zipfile` Module

The `zipfile` module provides tools for creating, reading, writing, appending,  
and listing ZIP archives.

### Creating a ZIP File

```python
import zipfile

files_to_zip = ['load_data.py', 'load_data2.py']

with zipfile.ZipFile('pyarchive.zip', 'w') as zip:
    for file in files_to_zip:
        zip.write(file)
```

**Explanation:**  
- `'w'` mode creates a new ZIP file (overwrites existing)  
- Each file is added using `write()` with its original name  
- The ZIP file is automatically closed when exiting the `with` block  

### Extracting a ZIP File

```python
import zipfile

with zipfile.ZipFile('output.zip', 'r') as zip_ref:
    zip_ref.extractall('tmp')
```

Extracts all contents of `output.zip` to the `tmp` directory. The `'r'` mode  
opens the ZIP for reading.

### Extracting Specific Files

```python
import zipfile

with zipfile.ZipFile('output.zip') as zip:
    zip.extract('funs.py', '.')
```

Extracts only the file `funs.py` to the current directory (`.`).

### Listing ZIP Contents

```python
import zipfile

with zipfile.ZipFile('output.zip') as zip:
    print(zip.namelist())
```

**Output:** `['load_data.py', 'load_data2.py', 'funs.py']`

### Appending to an Existing ZIP

```python
import zipfile

with zipfile.ZipFile('pyarchive.zip', 'a') as zip:
    print("Current files in the ZIP:", zip.namelist())

    new_file = 'newfile.txt'
    zip.write(new_file, arcname='newfile.txt')

    print("Updated files in the ZIP:", zip.namelist())
```

**Explanation:** The `'a'` (append) mode allows adding files to an existing  
archive without overwriting its contents.

---

## The `subprocess` Module

The `subprocess` module allows you to spawn new processes, connect to their  
input/output/error pipes, and obtain their return codes. It's the preferred  
way to run system commands from Python.

### Opening System Dialogs (Windows)

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

**Explanation:** This script opens the Windows System Properties dialog where  
environment variables can be edited. The `subprocess.run()` function executes  
the command in a shell, while `shell=True` allows the use of shell features.

> **Note:** Using `shell=True` can be a security risk if the command includes  
> user input. For production code, avoid it when possible.

---

## The `winreg` Module (Windows Registry Access)

**Note:** This module is **Windows-only** and considered **advanced**.  
Mac/Linux users can safely skip this section—it's not part of the standard  
library on those platforms.

The `winreg` module provides functions for working with the Windows Registry,  
allowing Python scripts to read and modify registry settings.

### Enabling Long Paths in Windows

```python
import winreg as reg
import ctypes
import os

def enable_long_paths():
    try:
        # Open the registry key
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
                          r"SYSTEM\CurrentControlSet\Control\FileSystem",
                          0,
                          reg.KEY_SET_VALUE)

        # Set the LongPathsEnabled value to 1
        reg.SetValueEx(key, "LongPathsEnabled", 0, reg.REG_DWORD, 1)

        # Close the registry key
        reg.CloseKey(key)

        print("Successfully enabled long paths in the registry.")

        # Check if the script has administrative privileges
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if not is_admin:
            print("Please run this script with administrative privileges for"
                  " the changes to take effect.")

    except PermissionError:
        print("Error: You need to run this script as an administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    enable_long_paths()
```

**Explanation of the code:**

1. **Registry Key:** Opens `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`  
2. **Setting Value:** `LongPathsEnabled` is set to `1` (enabled)  
3. **Admin Check:** Verifies if the script runs with administrator privileges  
4. **Error Handling:** Catches `PermissionError` when privileges are insufficient  

**Note:** This script requires administrative privileges to write to the  
registry. The change takes effect after a system restart.

---

## Putting It All Together

Now let's solve the five tasks from the introduction using the modules we've  
learned:

### Task 1: Read `PATH` and Find Python Content

```python
import os

path_var = os.environ.get("PATH", "")
path_dirs = path_var.split(os.pathsep)

python_paths = [p for p in path_dirs if "python" in p.lower()]
print("Python-related PATH entries:")
for p in python_paths:
    print(f"  {p}")
```

### Task 2: List All Python Files in Current Directory

```python
from pathlib import Path

py_files = list(Path.cwd().glob("*.py"))
print(f"Found {len(py_files)} Python files:")
for f in py_files:
    print(f"  {f.name}")
```

### Task 3: Display First 10 Python Files

```python
from pathlib import Path
from itertools import islice

py_files = Path.cwd().glob("*.py")
first_10 = list(islice(py_files, 10))

print("First 10 Python files:")
for i, f in enumerate(first_10, 1):
    print(f"{i:2}. {f.name}")
```

### Task 4: Fetch and Sort Words from URL, Filtering 'w' or 'c'

```python
import urllib.request
import urllib.error

url = 'https://webcode.me/words.txt'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        words = content.split()
        
        # Filter words starting with 'w' or 'c' (case-insensitive)
        filtered = [w for w in words if w.lower().startswith(('w', 'c'))]
        filtered.sort()
        
        print("Words starting with 'w' or 'c':")
        for w in filtered:
            print(f"  {w}")
            
except urllib.error.URLError:
    print("Error: Could not fetch words from the URL.")
```

### Task 5: Load JSON Data from URL into Dictionary

```python
import json
import urllib.request

url = 'https://webcode.me/users.json'

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        print("Loaded JSON data:")
        print(json.dumps(data, indent=2))
        
        # Process the data
        if isinstance(data, list):
            for user in data:
                print(f"User: {user.get('name', 'Unknown')}")
                
except urllib.error.URLError:
    print("Error: Could not fetch JSON data from the URL.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format received.")
```

---

## Best Practices Summary

| Module | Primary Use Case |
|--------|------------------|
| `os` | Environment variables and system operations |
| `pathlib` | Modern, object-oriented file path handling |
| `sys` | Accessing system-specific parameters and functions |
| `platform` | Getting platform/OS information |
| `json` | Working with JSON data (serialization/deserialization) |
| `urllib` | Making HTTP requests (standard library) |
| `secrets` | Generating cryptographically secure random data |
| `zipfile` | Creating and extracting ZIP archives |
| `subprocess` | Running external commands and programs |
| `winreg` | Windows Registry access (Windows-only, advanced) |


## Additional Resources

- [Python Standard Library Documentation](https://docs.python.org/3/library/index.html)  
- [Python Module of the Week (PyMOTW)](https://pymotw.com/3/)  
- [Real Python - Standard Library Guides](https://realpython.com/tutorials/python-standard-library/)  
- [Python's `pathlib` Documentation](https://docs.python.org/3/library/pathlib.html)  
- [Python's `urllib` Documentation](https://docs.python.org/3/library/urllib.html)  


*This document provides a practical introduction to Python's standard modules,  
equipping you with tools for common programming tasks. Experiment with the  
examples and consult the official documentation for more advanced features.*
