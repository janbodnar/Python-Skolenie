#!/usr/bin/python

from cerberus import Validator


v = Validator()
v.schema = {'words': {'type': ['string', 'list']}}

if v.validate({'words': 'falcon'}):
    print('valid data')
else:
    print('invalid data')

if v.validate({'words': ['falcon', 'sky', 'cloud']}):
    print('valid data')
else: 
    print('invalid data')
