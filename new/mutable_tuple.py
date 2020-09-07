#!/usr/bin/python

from collections.abc import Sequence


class MutableTuple(Sequence):
    """Abstract Base Class for objects that work like mutable
    namedtuples. Subclass and define your named fields with 
    __slots__ and away you go.
    """
    __slots__ = ()

    def __init__(self, *args):
        for slot, arg in zip(self.__slots__, args):
            setattr(self, slot, arg)

    def __repr__(self):
        return type(self).__name__ + repr(tuple(self))
    # more direct __iter__ than Sequence's

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)
    # Sequence requires __getitem__ & __len__:

    def __getitem__(self, index):
        return getattr(self, self.__slots__[index])

    def __len__(self):
        return len(self.__slots__)


class Student(MutableTuple):
    __slots__ = 'first', 'last', 'grade'  

student = Student('John', 'Doe', 'C')
print(student)

print(len(student))

print(student[0])
print(student[1])

for e in student:
    print(e)
