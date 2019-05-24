#!/usr/bin/env python3

import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('users.yaml', 'w') as f:
    
    data = yaml.dump(users, f)
