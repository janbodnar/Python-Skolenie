#!/usr/bin/python

import collections

Coin = collections.namedtuple('coin', ['rank'])

# a gold coin equals to two silver and six bronze coins


class Pouch:

    def __init__(self):
        self.bag = []

    def add(self, coin):

        self.bag.append(coin)

    def __eq__(self, other):

        val1, val2 = self.__evaluate(other)

        if val1 == val2:
            return True
        else:
            return False

    def __lt__(self, other):

        val1, val2 = self.__evaluate(other)
        # print(val1, val2)

        if val1 < val2:
            return True
        else:
            return False

    def __gt__(self, other):

        val1, val2 = self.__evaluate(other)
        # print(val1, val2)

        if val1 > val2:
            return True
        else:
            return False

    def __str__(self):

        return str(self.bag)

    def __evaluate(self, other):

        val1 = 0
        val2 = 0

        for coin in self.bag:

            if coin.rank == 'g':
                val1 += 6

            if coin.rank == 's':
                val1 += 3

            if coin.rank == 'b':
                val1 += 1

        for coin in other.bag:

            if coin.rank == 'g':
                val2 += 6

            if coin.rank == 's':
                val2 += 3

            if coin.rank == 'b':
                val2 += 1

        return val1, val2


pouch1 = Pouch()

pouch1.add(Coin('g'))
pouch1.add(Coin('g'))
pouch1.add(Coin('s'))

pouch2 = Pouch()

pouch2.add(Coin('g'))
pouch2.add(Coin('s'))
pouch2.add(Coin('s'))
pouch2.add(Coin('b'))
pouch2.add(Coin('b'))
pouch2.add(Coin('b'))

print(pouch1)
print(pouch2)

if pouch1 == pouch2:
    print('Pouches have equal value')

elif pouch1 > pouch2:
    print('Pouch 1 is more valueable than Pouch 2')
else:
    print('Pouch 2 is more valueable than Pouch 1')
