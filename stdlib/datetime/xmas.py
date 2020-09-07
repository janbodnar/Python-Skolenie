#!/usr/bin/python

from datetime import datetime

now = datetime.now()
xmas = datetime(now.year, 12, 25)
delta = xmas - now
final = delta.days

if final > 0:
    print(final, "days until XMas")
elif final == 0:
    print("Merry XMas!")
elif final < 0:
    print("It is past XMas, wait until next year!")
