# Object-oriented programming II


## Concepts

There are some basic programming concepts in OOP: 

- Abstraction
- Polymorphism
- Encapsulation
- Inheritance

The *abstraction* is simplifying complex reality by modeling classes appropriate to the problem.  
The *polymorphism* is the process of using an operator or function in different ways for different data input.  
The *encapsulation* hides the implementation details of a class from other objects. The *inheritance* is a way to  
form new classes using classes that have already been defined.  

## Class attributes

So far, we have been talking about instance attributes. In Python there are also so called class object  
attributes. Class object attributes are same for all instances of a class. 

```python
class Cat:
    species = 'mammal'

    def __init__(self, name, age):

        self.name = name
        self.age = age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy.name, missy.age)
print(lucky.name, lucky.age)

print(Cat.species)
print(missy.__class__.species)
print(lucky.__class__.species)
```

In our example, we have two cats with specific name and age attributes. Both cats share some characteristics.  
Missy and Lucky are both mammals. This is reflected in a class level attribute species. The attribute is defined  
outside any method name in the body of a class.

```python
print(Cat.species)
print(missy.__class__.species)
```

There are two ways how we can access the class object attributes: either via the name of the `Cat` class, or with the  
help of a special `__class__` attribute.

```
$ ./class_attribute.py 
Missy 3
Lucky 5
mammal
mammal
mammal
```

## Properties

The `@property` decorator in Python is a built-in decorator that allows us to  
use getter and setter methods as attributes, rather than methods. This provides  
a more intuitive and convenient way to handle instance variables.  

Here's an example of its usage with a `User` class that has `name` and  
`occupation` attributes:

```python
class User:
    def __init__(self, name='', occupation=''):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        if not isinstance(value, str):
            raise ValueError("Occupation must be a string.")
        self._occupation = value
```

In this example, `name` and `occupation` are property objects which provide an  
interface to the private `_name` and `_occupation` attributes. The `@property`  
decorator makes the method below it a getter for the property, and  
`@name.setter` and `@occupation.setter` decorators make the methods setters  
for the `name` and `occupation` properties. If you try to set the `name` or  
`occupation` to a non-string value, it raises a `ValueError`.

This approach allows for more control over how an attribute is accessed and  
modified, and can be used to implement validation and other property-specific  
logic.


## Ordering objects

The `__lt__` method is a special method used for overloading the less-than (`<`)  
operator. When it comes to sorting, this method is called to compare two objects  
and determine their order.

Defining only the `__lt__` method is sufficient for basic ordering functionality.  

Here's why:

Python leverages the defined `__lt__` method to implement the other comparison operators  
(`__gt__`, `__le__`, and `__ge__`) for your class.

Here's how it works:

- a > b is equivalent to not (a < b).
- a >= b is equivalent to not (a < b) or (a == b).
- a <= b is the opposite of a > b (can be derived from `__lt__` and `__eq__`).

Since Python can derive the other comparison methods from a well-defined `__lt__`, we only  
need to explicitly define `__lt__` for our custom class to enable ordering.  

However, there are some advantages to defining all the comparison methods explicitly:  

- Clarity: It can make your code more readable and express your intention clearly.  
- Customization: In rare cases, you might need to implement specific logic for each comparison.  


```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, User):
            return self.age < other.age
        return False
    
    def __str__(self):
        return f'[User {self.name} {self.age}]'

users = [User('Alice', 25), User('Bob', 20), User('Charlie', 22)]
users.sort()

for user in users:
    print(user)
```




## Ordering by multiple fields

```python
class User:
    def __init__(self, first_name, last_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

    def __lt__(self, other):
        if isinstance(other, User):
            if self.last_name == other.last_name:
                return self.first_name < other.first_name
            return self.last_name < other.last_name
        return False

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.occupation}'


users = [User('John', 'Doe', 'gardener'), User('Adam', 'Roe', 'student'), User('Jane', 'Doe', 'teacher'),
         User('Roger', 'Roe', 'driver'), User('John', 'Smith', 'broker'), User('Rob', 'Roe', 'dancer')]

# users.sort(key=lambda user: (user.last_name, user.first_name))
users.sort()

for user in users:
    print(user)
```

## Polymorphism

Polymorphism is the process of using an operator or function in different ways for different data input.   
In practical terms, polymorphism means that if class B inherits from class A, it doesn't have to inherit   
everything about class A; it can do some of the things that class A does differently.  

```python
a = "alfa"
b = (1, 2, 3, 4)
c = ['o', 'm', 'e', 'g', 'a']

print(a[2])
print(b[1])
print(c[3])
```

Python uses polymorphism extensively in built-in types. Here we use the same indexing operator for three  
different data types.

```
$ ./basic_polymorphism.py 
f
2
g
```

Polymorphism is mostly used when dealing with inheritance.

```python
#!/usr/bin/python

# polymorphism.py

class Animal:
    
   def __init__(self, name=''):
       
      self.name = name

   def talk(self):
       
      pass

class Cat(Animal):
    
   def talk(self):
       
      print("Meow!")

class Dog(Animal):
    
   def talk(self):
       
      print("Woof!")

a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()
```

Here we have two species: a dog and a cat. Both are animals. The `Dog` class and the `Cat` class inherit  
the `Animal` class. They have a `talk` method, which gives different output for them.

```
$ ./polymorphism.py 
Meow!
Woof!
```

## Enums

```python
from enum import Enum
import random


class Day(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    @staticmethod
    def random_day():
        return random.choice(list(Day.__members__.keys()))


days = [Day.Monday, Day.Tuesday, Day.Wednesday,
        Day.Thursday, Day.Friday, Day.Saturday, Day.Sunday]

res = random.sample(days, 4)

for e in res:

    match e:
        case Day.Monday:
            print("monday")
        case Day.Tuesday:
            print("tuesday")
        case Day.Wednesday:
            print("wednesay")
        case Day.Thursday:
            print("thursday")
        case Day.Friday:
            print("friday")
        case Day.Saturday:
            print("saturday")
        case Day.Sunday:
            print("sunday")

print('--------------------------------')

print(Day.random_day())
```

