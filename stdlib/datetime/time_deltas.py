#!/usr/bin/python

import datetime

now = datetime.datetime.now()

print(now)

dt1 = now + datetime.timedelta(days=1, hours=2)
print(dt1)

dt2 = now - datetime.timedelta(weeks=9)
print(dt2)
