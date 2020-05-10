#!/usr/bin/python

from multiprocessing import Process, Value, Lock

# adding values with lock produces
# the correct output

def add(val, lock):

    with lock:
        val.value += 1


def main():

    val = Value('i', 0)
    lock = Lock()

    processes = [Process(target=add, args=(val, lock)) for _ in range(200)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'Value is {val.value}')


if __name__ == "__main__":
    main()



