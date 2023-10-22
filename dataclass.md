# The dataclass 

The `dataclass` decorator is used to automatically generate special methods to classes, including  
`__str__` and `__repr__`. It helps reduce some boilerplate code. The `dataclass` decorator is  
located in the `dataclasses` module.  

The `dataclass` decorator examines the class to find fields. A field is defined as class variable  
that has a type annotation. 

```python
@dataclass
class Test:
...

@dataclass()
class Test:
...

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Test:
...
```

These three declarations are equivalent. If no parameters are set in the decorator, the default  
ones are used. If the init parameter is set to `True`, the `__init__` method will be generated.  
If the class already defines the `__init__`, the parameter is ignored. If the `repr` parameter  
is set to `True`, the `__repr__` method will be generated. If the class already defines the `__repr__`,  
the parameter is ignored. If the `eq` parameter is set to `True`, the `__eq__` method will be generated.  
If the class already defines `__eq__`, this parameter is ignored.

If the order parameter is set to `True`, the `__lt__`, `__le__`, `__gt__`, and `__ge__` methods are generated.  
If the class already defines any of the methods, the ValueError is raised. If the `unsafe_hash` is defined  
to `False`, the `__hash__` method is generated according to how eq and frozen are set. If the `frozen` parameter  
is set to `True`, the assignment to fields will generate an exception. 

## Regular custom class

In a regular custom Python class, we provide a constructor and other methods such as `__repr__` manually.

```python
#!/usr/bin/python

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):

        return f'Person{{name: {self.name}, age: {self.age}}}'


p = Person('John Doe', 34)
print(p)
```

The example shows a `Person` class with a constructor and the `__repr__` method, which gives  
a complete representation of the object.  

```
$ ./regular_class.py
Person{name: John Doe, age: 34}
```

## The dataclass example

The following example shows a simple usage of the `dataclass` decorator.

```python
#!/usr/bin/python

# simple_dataclass.py

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person('John Doe', 34)
print(p)
```

We have a class with two fields: `name` and `str`.

```python
from dataclasses import dataclass
```

The `dataclass` decorator is located in the dataclasses module.

```python
@dataclass
class Person:
    name: str
    age: int
```

We apply the dataclass decorator on the `Person` class.

```
p = Person('John Doe', 34)
print(p)
```

A new person object is created. Its `__init__` method is called, which is auto-generated  
by the `dataclass` decorator.

```
$ ./simple_dataclass.py
Person(name='John Doe', age=34)
Python dataclass default values
```

It is possible to provide default values to the fields.

```python
#!/usr/bin/python

# default_values.py

from dataclasses import dataclass

@dataclass
class Person:
    name: str = 'unknown'
    age: int = 0

p = Person('John Doe', 34)
print(p)

p2 = Person()
print(p2)
```

In the example, the `Person` class has two fields; the fields have some default values.

```python
@dataclass
class Person:
    name: str = 'unknown'
    age: int = 0
```

With the assignment operator `=`, we give the fields default values.

```python
p2 = Person()
print(p2)
```

When we do not provide values in the constructor, the fields will have default values.

```
$ ./default_values.py
Person(name='John Doe', age=34)
Person(name='unknown', age=0)
```

## The frozen parameter

If the frozen parameter is set to True, we cannot assign values to fields.

```python
#!/usr/bin/python

# frozen.py

from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person('John Doe', 34)
p.occupation = 'gardener'

print(p)
print(p.occupation)
```


In the example, the frozen parameter is set to `True`. The program fails with the following error message:  
*dataclasses.FrozenInstanceError: cannot assign to field 'occupation'.*

## The asdict function

The `asdict` function converts a dataclass instance to a dict of its fields.

```python
#!/usr/bin/python

from dataclasses import dataclass, asdict

# as_dict_fun.py

@dataclass
class Person:
    name: str
    occupation: str
    age: int

p = Person('John Doe', 'gardener', 34)
print(p)

print(asdict(p))
```

In the example, we print the fields of the Person class with the help of the `asdict` function.

```
$ ./as_dict_fun.py
Person(name='John Doe', occupation='gardener', age=34)
{'name': 'John Doe', 'occupation': 'gardener', 'age': 34}
```

The first line is the output of the `__repr__` method. The second line is the dictionary of the fields.

## The field function

With the `field` function, we can provide some additional per-field information.

```python
#!/usr/bin/python

# fields.py

from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    occupation: str = field(init=False, repr=False)

p = Person('John Doe', 34)
print(p)

p.occupation = "Gardener"
print(f'{p.name} is a {p.occupation}')
```

In the example, we have an additional occupation field.

```python
occupation: str = field(init=False, repr=False)
The occupation field is not included in the __init__ and __repr__ methods.
```

```
$ ./fields.py
Person(name='John Doe', age=34)
John Doe is a Gardener
```

## Pattern match

The next example uses a data class with pattern matching syntax.

```python
#!/usr/bin/python

# points.py

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


def check(p):
    match p:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x, y) if y == 0:
            print(f"on x axis")
        case Point(x, y) if x == 0:
            print(f"on y axis")
        case Point(x, y) if x > 0 and y > 0:
            print("Q I")
        case Point(x, y) if x < 0 and y > 0:
            print("Q II")
        case Point(x, y) if x < 0 and y < 0:
            print("Q III")
        case Point(x, y) if x > 0 and y < 0:
            print("Q IV")
        case _:
            print("Not a point")


points = [Point(3, 0), Point(0, 0), Point(-4, -5), Point(-4, 0), Point(0, 5),
          Point(4, 8), Point(-5, 3), Point(6, -4)]

for p in points:
    check(p)
```

We have a list of `Point` objects. With `match/case` keywords, we assign each point to the  
origin, `x` and `y` axis, or one of the four quadrants.

```python
case Point(x=0, y=0):
    print("Origin")
```

In this case arm, we match against a point which has x=0 and y=0 coordinates.

```python
case Point(x, y) if x > 0 and y > 0:
    print("Q I")
```
   
Using guards, we check if the point lies in the first quadrant.

```
$ ./points.py 
on x axis
Origin
Q III
on x axis
on y axis
Q I
Q II
Q IV
```
