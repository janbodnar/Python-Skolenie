#!/usr/bin/env python3

from cerberus import Validator
import yaml

v = Validator()
v.schema = {'cities': {'type': 'list', 'schema': {'type': 'string'}}}

with open('cities.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    if v.validate({'cities': data['cities']}):
        print('valid data')
    else:
        print('invalid data')
        print(v.errors)



