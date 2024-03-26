# Test example

```python
#!/usr/bin/python

import json
import requests
from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str


url = 'https://webcode.me/users.json'

resp = requests.get(url)

data = resp.content.decode('utf8')
users_dict = json.loads(data)

users = []

for e in users_dict['users']:
    users.append(User(**e))
    # users.append(User(e['id'], e['first_name'],
    #              e['last_name'], e['email']))

for e in users:
    print(e)
```
