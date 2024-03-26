# Test example

```python
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
        case User(fname, lname, 'student'):
            print(f'{user.fname} {user.lname} is a student')
```
