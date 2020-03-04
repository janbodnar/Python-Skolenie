#!/usr/bin/env python

def myfun():
    print("inside myfun()")

    def greet():
        return "greeting message"

    def welcome():
        return "welcoming message"

    print(greet())
    print(welcome())
    print("inside myfun()")

myfun()
