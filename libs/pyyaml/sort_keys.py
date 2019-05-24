#!/usr/bin/env python3

import yaml

with open('items.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    sorted = yaml.dump(data, sort_keys=True)
    print(sorted)
