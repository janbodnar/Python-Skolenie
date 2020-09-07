#!/usr/bin/python

from cerberus import Validator

v = Validator()
v.schema = {'name': { 'type': 'string', 'minlength': 2}, 
    'age': {'type': 'integer', 'min': 18, 'max': 65}}

if v.validate({'name': 'J', 'age': 4}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)
