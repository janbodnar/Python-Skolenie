#!/usr/bin/python3

# read_excel_cells.py

import openpyxl

wb = openpyxl.load_workbook('psc.xlsx')
print (wb.get_sheet_names())

sheet = wb.get_sheet_by_name('PSČ')
c1 = sheet['A1']
print (c1.value)

c2 = sheet['B1']
c2.value
print(type(c2.value))

print (str(c2.value))

c3 = sheet['B3']
c3.value

print(type(c3.value))
