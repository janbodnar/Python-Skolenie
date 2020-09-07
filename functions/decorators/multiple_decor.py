#!/usr/bin/python

def start(fun):

    def inner():

        print("***************************")
        fun()

    return inner


def end(fun):

    def inner():

        fun()
        print("***************************")

    return inner

@start
@end
def myfun():
    print("myfun")

myfun()

# def myfun():
#     print("myfun")

# f = start(end(myfun))
# f()
