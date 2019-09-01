#!/usr/bin/env python3

from cerberus import Validator


v = Validator()
v.schema = {'name': {'required': True, 'type': 'string'}, 'age': {'type': 'integer'}}

if v.validate({'age': 34}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)
