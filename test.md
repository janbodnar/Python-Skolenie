# Test example

```python
#!/usr/bin/python

# nacitat
# JSON - Dict
# Dict - list of dataclass objects

import json
import requests

url = 'https://webcode.me/users.json'

resp = requests.get(url)

data = resp.content.decode('utf8')
users_dict = json.loads(data)  

print(users_dict['users'])





```
