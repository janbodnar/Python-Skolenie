#!/usr/bin/python

import yaml

with open('items.yaml') as f:
    
    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)
