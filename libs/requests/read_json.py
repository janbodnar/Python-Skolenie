#!/usr/bin/python

import requests as req

resp = req.get('https://jsonplaceholder.typicode.com/posts')
json_list = resp.json()

for e in json_list:
    print('Id: {}'.format(e['id']))
    print('Title: {}'.format(e['title']))
    print('Body: {}'.format(e['body']))
