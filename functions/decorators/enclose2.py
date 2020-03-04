#!/usr/bin/env python

def enclose(fun):

    def wrapper():

        print("***************************")
        fun()
        print("***************************")

    return wrapper

@enclose
def myfun():
    print("myfun")

myfun()
