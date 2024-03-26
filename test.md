# Test example

```python

from dataclasses import dataclass

# nacitat data
# vytvorit list dataclass objektov
# for loop -> vypis vsetkych studentov

# open, Path


@dataclass
class User:
    fname: str
    lname: str
    occupation: str


users = []

fname = 'users.txt'
with open(fname, 'r') as f:

    rows = []

    lines = f.readlines()
    lines2 = [e.strip() for e in lines if e.strip()]
    for e in lines2:
        parts = e.split(',')

        users.append(User(parts[0], parts[1], parts[2]))


for user in users:
    match user:
        case User(fname, lname, 'teacher') | User(fname, lname, 'driver'):
            print(f'{user.fname} {user.lname} is a teacher or driver')
```
