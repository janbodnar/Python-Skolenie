# Priklady 22.10.2024

## Nacitanie CSV data

Tento priklad stahune data z CSV suboru na webe.  

Pouzivame:

- dataclass
- requests modul

```python
from dataclasses import dataclass
import requests

@dataclass(frozen=True)
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str

url = 'https://webcode.me/users.csv'

resp = requests.get(url)
content = resp.content.decode('utf8')

lines = content.splitlines()

users = []

for line in lines[1:-1]:
    fields = line.split(',', 3)
    fields_cleaned = fields[0], fields[1], fields[2], fields[3].replace('"', '')

    u = User(*fields_cleaned)
    users.append(u)


for user in users:
    print(user)
```
