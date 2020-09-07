#!/usr/bin/python

def enclose(fun):

    def wrapper():

        print("***************************")
        fun()
        print("***************************")

    return wrapper

def myfun():
    print("myfun")

enc = enclose(myfun)
enc()
