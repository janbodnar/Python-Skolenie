#!/usr/bin/env python3

import yaml

with open('items.yaml') as f:
    
    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)
