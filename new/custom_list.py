#!/usr/bin/env python

class MyList:

    def __init__(self, elements=0):
        self.mylist = [0] * elements

    def __setitem__(self, index, value):
        self.mylist[index] = value

    def __getitem__(self, index):
        return  self.mylist[index]

    def __len__(self):
        return len(self.mylist)

    def __str__(self):
        return str(self.mylist)

    def __repr__(self):
        return f'MyList: {str(self)}'

ml = MyList(12)
ml[0] = 1
ml[1] = 2
ml[2] = 3

print(len(ml))

print(ml[0])
print(ml)

print(repr(ml))
