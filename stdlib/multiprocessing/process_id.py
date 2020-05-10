#!/usr/bin/python

from multiprocessing import Process
import os

# getting parent and child process Ids


def fun():

    print('--------------------------')

    print('calling fun')
    print('parent process id:', os.getppid())
    print('process id:', os.getpid())

def main():

    print('main fun')
    print('process id:', os.getpid())

    p1 = Process(target=fun)
    p1.start()
    p1.join()

    p2 = Process(target=fun)
    p2.start()
    p2.join()


if __name__ == '__main__':
    main()
