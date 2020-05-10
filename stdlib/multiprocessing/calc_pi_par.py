#!/usr/bin/python

from decimal import Decimal, getcontext
from timeit import default_timer as timer
from multiprocessing import Pool, current_process
import time

# calculating pi sequentially with 
# Bailey–Borwein–Plouffe formula


def pi(precision):

    getcontext().prec=precision

    return sum(1/Decimal(16)**k *
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range (precision))


def main():

    start = timer()

    with Pool(3) as pool:

        values = (1000, 1500, 2000)
        data = pool.map(pi, values)
        print(data)

    end = timer()
    print(f'paralelly: {end - start}')


if __name__ == '__main__':
    main()
