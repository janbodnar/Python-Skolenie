#!/usr/bin/python

from datetime import datetime

import pytz
local = datetime.now()

print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
tz_MSC = pytz.timezone('Europe/Moscow') 

datetime_NY = datetime.now(tz_MSC)
print("Moscow:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)

print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
