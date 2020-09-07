#!/usr/bin/python

def enclose(fun):

    def wrapper(val):

        print("***************************")
        fun(val)
        print("***************************")

    return wrapper

@enclose
def myfun(val):
    print(f"myfun with {val}")

myfun('falcon')
