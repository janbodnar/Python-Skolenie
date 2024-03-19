# Types


## The type function

```python
#!/usr/bin/python

import sys


class Being:
    pass


def function():
    pass


objects = [
    1,
    3.4,
    sys,
    function,
    range(10),
    None,
    False,
    [1, 2],
    "Python",
    (2, 3),
    Being(),
    {},
]

for e in objects:
    print(type(e))
```


## Check types

```python
#!/usr/bin/python

class Being:
    pass


objects = [1, -2, 3.4, None, False, [1, 2], "Python", (2, 3), Being(), {}]

for e in objects:
    match e:
        case None:
            print(f'{e} is a null value')
        case list():
            print(f'{e} is a list cointainer')
        case tuple():
            print(f'{e} is a tuple cointainer')
        case float():
            print(f'{e} is a float')
        case True | False:
            print(f'{e} is a boolean value')
        case _val if isinstance(_val, str):
            print(f'{e} is a string')
        case _val if isinstance(_val, dict):
            print(f'{e} is a dictionary')
        case _val if isinstance(_val, int):
            print(f'{e} is an integer')
```


## Type hints

### Tuples

```python
#!/usr/bin/python


vals: tuple[int, ...] = (1, 2, 3, 4, 5, 4)
print(max(vals))

vals2: tuple[int, int, int] = (1, 2, 3)
print(min(vals))
```

### Lists

```python
#!/usr/bin/python

from typing import Any


vals: list[Any] = [1, "falcon", True]
print(vals)

vals2: list[int] = [1, 2, 3, 4, 4]
print(vals2)

vals3: list[bool] = [True, False, True, True]
print(vals3)

vals4: list[float] = [1.0, 2, 3.4, 0, -1, 9]
print(vals4)
```

### Literals

```python
#!/usr/bin/python

from typing import Literal

type Mode = Literal["r", "w", "a", "rw"]


def read_file(name: str, fmode: Mode) -> str:
    return "content"


content: str = read_file("dummy.txt", "r")
print(content)
```

### Function parameters 

```python
#!/usr/bin/python

def add(x: int, y: int) -> int:
    return x + y


print(add(2, 5))
```

### Unions

```python
#!/usr/bin/python

vals: list[int | float] = [1, 3.4, 4]
print(vals)

vals2: list[str | bool] = ["falcon", "war", True, False]
print(len(vals2))
```


### Type alias

```python
#!/usr/bin/python


type Num = int | float

vals: list[Num] = [1, 3.4, 4, 6, 3.2]
print(vals)
```


### Complex example

```python
#!/usr/bin/python

from dataclasses import dataclass
from random import randint


type Users = list[User]


@dataclass
class User:
    name: str
    occupation: str

    @staticmethod
    def rand_users(n: int) -> Users:
        return Helper.generate_users(n)


class Helper:
    @staticmethod
    def get_usernames() -> list[str]:
        names: list[str] = [
            "John Doe",
            "Roger Roe",
            "Martin Biely",
            "Susan Kelly",
            "Paul Smith",
            "Tom Nolland",
            "Lucia Smith",
            "Tibor Novak",
        ]

        return names

    @staticmethod
    def get_occupations() -> list[str]:
        occupations: list[str] = [
            "gardener",
            "driver",
            "teacher",
            "shopkeeper",
            "scientist",
            "programmer",
            "optician",
        ]
        return occupations

    @staticmethod
    def generate_users(n: int) -> Users:
        names: list[str] = __class__.get_usernames()
        occupations: list[str] = Helper.get_occupations()
        n1: int = len(names) - 1 
        n2: int = len(occupations) - 1
        users: Users = []

        for _ in range(n):
            users.append(User(names[randint(0, n1)], occupations[randint(0, n2)]))

        return users


users: Users = User.rand_users(4)
print(users)
```



