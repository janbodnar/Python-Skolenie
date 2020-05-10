#!/usr/bin/python

from multiprocessing import Process, Value

# adding without using lock
# gives erroneous output

def add(val):
    val.value += 1


def main():

    val = Value('i', 0) 

    processes = [Process(target=add, args=(val, )) for _ in range(200)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'Value is {val.value}')


if __name__ == "__main__":
    main()
