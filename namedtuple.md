# Python namedtuple



Here's the text rewritten into markdown code with about 80 characters per line, each line ending in two spaces:


## Differences between Python classes and namedtuples

### Purpose  

- class: A general-purpose construct for creating objects that encapsulate  
data (attributes) and behavior (methods). Classes are fundamental for  
object-oriented programming (OOP) in Python. They allow you to define the  
blueprint for creating objects with specific attributes and functionalities.  

- Namedtuple: A lightweight data structure specifically designed to hold  
collections of data with named fields. They are essentially immutable tuples  
with a more user-friendly way of accessing elements by name. Namedtuples are  
ideal for simple data containers where you don't need complex methods or  
object behavior.  

### Mutability

- Class: Instances of a class can be mutable by default. This means you can  
modify the values of their attributes after they are created.  

- Namedtuple: Namedtuples are immutable. Once created, you cannot change the  
values of their elements.  

### Methods

- class: Classes can define methods (functions) that operate on the object's  
data or provide functionalities specific to that object type.  

- Namedtuple: Namedtuples do not have built-in methods. However, they inherit  
some basic methods from tuples since they are a subclass of tuples.  

### Creation  

- class: Classes are defined using the class keyword followed by the class name  
and optionally inheritance specifications. You then define the attributes and  
methods within the class body.  

- Namedtuple: Namedtuples are created using the namedtuple function from the  
collections module. You provide a name for the tuple type and a list of field  
names. The namedtuple function automatically generates a class representing  
the namedtuple.  

### Example

Using a Class:  

```python
class Person:  
  def __init__(self, name, age):  # Constructor (initialization method)  
    self.name = name  
    self.age = age  

  def greet(self):  # Method to define object behavior  
    print(f"Hello, my name is {self.name}!")  

person1 = Person("Alice", 30)  
person1.greet()  # Output: Hello, my name is Alice!  
```

Using a Namedtuple:  

```python
from collections import namedtuple  

# Define namedtuple  
Point = namedtuple('Point', ['x', 'y'])  

# Create point instances  
point1 = Point(10, 20)  
point2 = Point(3, 5)  

# Access elements by name  
print(point1.x)  # Output: 10  
print(point2.y)  # Output: 5  

# Namedtuples are immutable (attempting to modify will raise an error)  
# point1.x = 15  # This will cause an error  
```

### Choosing between a class and Namedtuple: 

Use a class if you need to create objects with:  

- Custom behavior through methods  
- Mutable attributes that can change after creation  
- Inheritance for code reusability  

Use a namedtuple if you need a simple, lightweight data container with:  

- Named fields for easy access  
- Immutability for data integrity  

In essence, classes offer more flexibility and power for complex  
object-oriented programming, while namedtuples provide a concise way to hold  
named data collections.  
