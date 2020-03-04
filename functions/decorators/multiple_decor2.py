#!/usr/bin/env python


def strong(fun):

    def wrapper():
        return f'<strong>{fun()}</strong>'
    return wrapper

def em(fun):

    def wrapper():
        return f'<em>{fun()}</em>'

    return wrapper


@strong
@em
def message():
    return 'This is some message'


print(message())
