#!/usr/bin/python

from datetime import datetime
a = datetime(2019, 9, 15, 22, 3, 31, 355741)

print(f'year: {a.year}')
print(f'month: {a.month}')
print(f'hour: {a.hour}')
print(f'minute: {a.minute}')
print(f'timestamp: {a.timestamp()}')
