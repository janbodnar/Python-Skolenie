#!/usr/bin/python3

import locale
from functools import cmp_to_key

w = [u'zem', u'štebot', u'rum', u'železo', u'prameň', u"sob"]
locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))

w.sort(key=cmp_to_key(locale.strcoll))

for e in w:
    print (e)
