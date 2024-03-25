# Object-oriented programming


There are three widely used programming paradigms there: procedural programming,  
functional programming, and object-oriented programming. Python supports all three  
programming paradigms. 

## Object-oriented programming

*Object-oriented programming (OOP)* is a programming paradigm that uses objects and their  
interactions to design applications and computer programs.  

There are some basic programming concepts in OOP: 

- Abstraction
- Polymorphism
- Encapsulation
- Inheritance

The *abstraction* is simplifying complex reality by modeling classes appropriate to the problem.  
The *polymorphism* is the process of using an operator or function in different ways for different data input.  
The *encapsulation* hides the implementation details of a class from other objects. The *inheritance* is a way to  
form new classes using classes that have already been defined.  

## Objects

Everything in Python is an object. Objects are basic building blocks of a Python OOP program.  

```python
#!/usr/bin/python

# object_types.py

import sys

def function():
    pass

print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))
print(type(function))
print(type(sys))
```

In this example we show that all these entities are in fact objects. The `type` function returns the 
type of the object specified.

```
$ ./object_types.py 
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'type'>
<class 'function'>
<class 'module'>
```

Integers, strings, lists, dictionaries, tuples, functions, and modules are Python objects.  

## The class keyword

The previous objects were all built-in objects of the Python programming language. The user  
defined objects are created using the class keyword. The class is a blueprint that defines  
a nature of a future object. From classes we construct instances. An instance is a specific  
object created from a particular class. For example, Huck might be an instance of a Dog class.

```python
#!/usr/bin/python

# first_object.py

class First:
    pass

fr = First()

print(type(fr))
print(type(First))
```

This is our first class. The body of the class is left empty for now. It is a convention to give  
classes a name that starts with a capital letter. 

```python
class First:
    pass
```

Here we define the `First` class. Note that by default, all classes inherit from the base object.  

```python
fr = First()
```

Here we create a new instance of the `First` class. Or in other words, we instantiate the `First` class.  
The `fr` is a reference to our new object.

```
$ ./first_object.py 
<class '__main__.First'>
<class 'type'>
```

Here we see that `fr` is an instance object of the `First` class.

Inside a class, we can define attributes and methods. An attribute is a characteristic of an object.  
This can be for example a salary of an employee. A method defines operations that we can perform with our objects.  
A method might define a cancellation of an account. Technically, attributes are variables and methods are  
functions defined inside a class.

## Object initialization

A special method called `__init__` is used to initialize an object.  

```python
#!/usr/bin/python

# object_initialization.py

class Being:

    def __init__(self):
        print("Being is initialized")

Being()
```

We have a Being class. The special method `__init__` is called automatically right after the object has been created.  

```
$ ./object_initialization.py 
Being is initialized
```

## Object attributes

Attributes are characteristics of an object. Attributes are set in the `__init__` method.

```python
#!/usr/bin/python

# attributes.py

class Cat:

    def __init__(self, name):

        self.name = name

missy = Cat('Missy')
lucky = Cat('Lucky')

print(missy.name)
print(lucky.name)
```

In this code example, we have a Cat class. The special method `__init__` is called automatically right after  
the object has been created.

```python
def __init__(self, name):
```

Each method in a class definition begins with a reference to the instance object. It is by convention named `self`.  
There is nothing special about the self name. We could name it this, for example. The second parameter, name,  
is the argument. The value is passed during the class initialization.  

```python
self.name = name
```

Here we pass an attribute to an instance object.

```python
missy = Cat('Missy')
lucky = Cat('Lucky')
```

Here we create two objects: cats Missy and Lucky. The number of arguments must correspond to the `__init__` method  
of the class definition. The 'Missy' and 'Lucky' strings become the name parameter of the `__init__` method.  

```python
print(missy.name)
print(lucky.name)
```

Here we print the attributes of the two cat objects. Each instance of a class can have their own attributes.

```
$ ./attributes.py 
Missy
Lucky
```

The attributes can be assigned dynamically, not just during initialization. This is demonstrated by the next example.  

```python
#!/usr/bin/python

# attributes_dynamic.py

class Person:
    pass

p = Person()
p.age = 24
p.name = "Peter"

print("{0} is {1} years old".format(p.name, p.age))
```

We define and create an empty `Person` class.

```python
p.age = 24
p.name = "Peter"
```

Here we create two attributes dynamically: `age` and `name`.

```
$ ./attributes_dynamic.py 
24 is Peter years old
```

## Class attributes

So far, we have been talking about instance attributes. In Python there are also so called class object  
attributes. Class object attributes are same for all instances of a class. 

```python
#!/usr/bin/python

# class_attribute.py

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

## Methods

Methods are functions defined inside the body of a class. They are used to perform operations with the attributes  
of our objects. Methods are essential in the encapsulation concept of the OOP paradigm. For example, we might have  
a connect method in our AccessDatabase class. We need not to be informed how exactly the method connect connects  
to the database. We only know that it is used to connect to a database. This is essential in dividing responsibilities  
in programming, especially in large applications.

```python
#!/usr/bin/python

# methods.py

class Circle:

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())
```

In the code example, we have a `Circle` class. We define three new methods.

```python
def area(self):
    return self.radius * self.radius * Circle.pi
```

The area method returns the area of a circle.

```python
def setRadius(self, radius):
    self.radius = radius
```

The `setRadius` method sets a new value for the radius attribute.

```python
def getRadius(self):
    return self.radius
```

The `getRadius` method returns the current radius.  

```python
c.setRadius(5)
```

The method is called on an instance object. The c object is paired with the `self` parameter  
of the class definition. The number 5 is paired with the `radius` parameter.  

```
$ ./methods.py 
5
78.5398
```

In Python, we can call methods in two ways. There are bounded and unbounded method calls.

```python
#!/usr/bin/python

# bound_unbound_methods.py

class Methods:

    def __init__(self):
        self.name = 'Methods'

    def getName(self):
        return self.name


m = Methods()

print(m.getName())
print(Methods.getName(m))
```

In this example, we demostrate both method calls.

```python
print(m.getName())
```

This is the bounded method call. The Python interpreter automatically pairs the `m` instance  
with the `self` parameter.

```python
print(Methods.getName(m))
```

And this is the unbounded method call. The instance object is explicitly given to the `getName` method.  

```
$ ./bound_unbound_methods.py 
Methods
Methods
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


## Object equality 

The object equality is determined by the `__eq__` method. By default, this method  
checks if two objects are the same object (i.e., they occupy the same memory space).  
However, we can override the `__eq__` method in your class to define custom equality logic. 

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.age == other.age
        return False

u1 = User("John Doe", 35)
u2 = User("John Doe", 35)

u3 = u1

print(u1 == u2)  
print(u1 == u3)  
```

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



## Inheritance

Inheritance is a way to form new classes using classes that have already been defined. The newly formed   
classes are called derived classes, the classes that we derive from are called base classes. Important  
benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes  
(descendants) override or extend the functionality of base classes (ancestors).   

```python
#!/usr/bin/python

# inheritance.py

class Animal:

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()
```

In this example, we have two classes: `Animal` and `Dog`. The `Animal` is the base class, the `Dog` is the derived class.  
The derived class inherits the functionality of the base class. It is shown by the eat method. The derived class  
modifies existing behaviour of the base class, shown by the whoAmI method. Finally, the derived class extends the  
functionality of the base class, by defining a new bark method. 

```python
class Dog(Animal):

    def __init__(self):
        super().__init__()
        
        print("Dog created")
```

We put the ancestor classes in round brackets after the name of the descendant class. If the derived class provides its  
own `__init__` method and we want to call the parent constructor, we have to explicitly call the base class `__init__`  
method with the help of the super function.  

```
$ ./inherit.py 
Animal created
Dog created
Dog
Eating
Woof!
```

## Polymorphism

Polymorphism is the process of using an operator or function in different ways for different data input.   
In practical terms, polymorphism means that if class B inherits from class A, it doesn't have to inherit   
everything about class A; it can do some of the things that class A does differently.  

```python
#!/usr/bin/python

# basic_polymorphism.py

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

## Python special methods

Classes in Python programming language can implement certain operations with special method names.  
These methods are not called directly, but by a specific language syntax. This is similar to what  
is known as operator overloading in C++ or Ruby.

```python
#!/usr/bin/python

# special_methods.py

class Book:

    def __init__(self, title, author, pages):

        print("A book is created")

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return "Title:{0} , author:{1}, pages:{2} ".format(
            self.title, self.author, self.pages)

    def __len__(self):

        return self.pages

    def __del__(self):

        print("A book is destroyed")

book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print(book)
print(len(book))
del book
```

In our code example, we have a book class. Here we introduce four special methods: `__init__`, `__str__`,  
`__len__` and `__del__`.

```python
book = Book("Inside Steve's Brain", "Leander Kahney", 304)
```

Here we call the `__init__` method. The method creates a new instance of a `Book` class.

```python
print(book)
```

The `print` function calls the `__str__` method. This method should return an informal string representation of an object.

```python
print(len(book))
```

The len function invokes the `__len__` method. In our case, we print the number of pages of our book.

```python
del book
```

The `del` keyword deletes an object. It invokes its `__del__` method.


In the next example we implement a vector class and demonstrate addition and substraction operations on it.

```python
#!/usr/bin/python

# vector.py

class Vector:

    def __init__(self, data):

        self.data = data

    def __str__(self):

        return repr(self.data)

    def __add__(self, other):

        data = []

        for j in range(len(self.data)):

            data.append(self.data[j] + other.data[j])

        return Vector(data)

    def __sub__(self, other):

        data = []

        for j in range(len(self.data)):

            data.append(self.data[j] - other.data[j])

        return Vector(data)


x = Vector([1, 2, 3])
y = Vector([3, 0, 2])

print(x + y)
print(y - x)
```

The example presents `__add__` and `__sub__` methods.

```python
def __add__(self, other):

    data = []

    for j in range(len(self.data)):

        data.append(self.data[j] + other.data[j])

    return Vector(data)
```

Here we implement the addition operation of vectors. The `__add__` method is called when we add two `Vector`  
objects with the `+` operator. Here we add each member of the respective vectors.  

```
$ ./vector.py 
[4, 2, 5]
[2, -2, -1]
```
