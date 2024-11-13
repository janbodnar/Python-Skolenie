# Priklady

```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
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


## Pandas read CSV from URL

```python
import pandas
import requests
from io import StringIO

url = 'https://webcode.me/users.csv'
resp = requests.get(url)
content = resp.content.decode('utf8')

csv_file = StringIO(content)

df = pandas.read_csv(csv_file)
print(df.head(20))
```


## splitlines

```python
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

lines = data.splitlines()
lines.pop(0)

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```

## StringIO

```python
from io import StringIO

# calculate sum
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

# with open('words.txt', 'r') as f:
#    lines = f.readlines()


fdata = StringIO(data)

lines = fdata.readlines()
lines.pop(0)

lines = [line.strip() for line in lines]

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```

## Read CSV from URL using StringIO


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

users = []

fcsv = StringIO(content)
reader = csv.DictReader(fcsv)

for line in reader:
    u = User(int(line['id']), line['first_name'],
             line['last_name'], line['occupation'])
    # u = User(**line)
    users.append(u)


users_w = [user for user in users if user.last_name.startswith(('W', 'A'))]
print(users_w)
```


