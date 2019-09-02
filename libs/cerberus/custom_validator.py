#!/usr/bin/env python3

from cerberus import Validator
from dataclasses import dataclass

# class Person:

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age


@dataclass
class Person:
    name: str
    age: int

class PersonValidator(Validator):

     def validate_person(self, obj):

         return self.validate(obj.__dict__)

schema = {'name': { 'type': 'string', 'minlength': 2},
    'age': {'type': 'integer', 'min': 18, 'max': 65}}

v = PersonValidator(schema)

p = Person('John Doe', 2)


if v.validate_person(p):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)

