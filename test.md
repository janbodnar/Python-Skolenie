# Test example

```python
#!/usr/bin/python

# nacitat
# JSON - Dict
# Dict - list of dataclass objects

import requests

url = 'https://webcode.me/users.json'

resp = requests.get(url)

data = resp.content.decode('utf8')

print(data)





```
