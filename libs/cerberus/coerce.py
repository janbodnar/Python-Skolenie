#!/usr/bin/python

from cerberus import Validator
from datetime import datetime


def to_date(s):
    return datetime.strptime(s, '%Y-%m-%d')


v = Validator()
v.schema = {'start_date': {'type': 'datetime', 'coerce': to_date}}

if v.validate({'start_date': '2019-12-11'}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)

if v.validate({'start_date': '2019/12/11'}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)

