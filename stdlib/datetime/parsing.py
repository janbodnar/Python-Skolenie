#!/usr/bin/python

from datetime import datetime

dt1 = datetime.strptime('Jun 1 2018 5:33PM', '%b %d %Y %I:%M%p')
print(dt1)

dt2 = datetime.strptime('23:33:45', '%H:%M:%S')
print(dt2.time())
