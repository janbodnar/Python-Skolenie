#!/usr/bin/python

import shutil

total_b, used_b, free_b = shutil.disk_usage('.')

gb = 10 ** 9 # GB == gigabyte

print('Total: {:6.2f} GB'.format(total_b / gb))
print('Used : {:6.2f} GB'.format(used_b / gb))
print('Free : {:6.2f} GB'.format(free_b / gb))
