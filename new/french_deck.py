#!/usr/bin/python

import collections
from random import choice


Card = collections.namedtuple('Card', ['suit', 'rank'])


class FrenchDeck:

    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ["heart", "clubs", "spades", "diamond"]

    def __init__(self):
        self.total = [Card(suit, rank)
                           for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.total)

    def __getitem__(self, index):
        return self.total[index]


deck = FrenchDeck()
print(deck[0])
# print(deck[2:7])
# print(deck[-2])
print(len(deck))
print(choice(deck))

# namedtuple is a factory function for making a tuple class. With that class we
# can create tuples that are callable by name also.

# It's a specific subclass of a tuple that is programmatically created to your
# specification, with named fields and a fixed length.
