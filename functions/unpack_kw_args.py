#!/usr/bin/python

def display(**user):

    for k, v in user.items():
        print(f'{k}: {v}')


display(name='Lary Jones', age=43, sex='M')
display(name='Jone Doe', occupation='gardener', age=35)
