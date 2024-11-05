# Openpyxl

The openpyxl is a Python library to read and write Excel 2010  
xlsx/xlsm/xltx/xltm files.

# Excel xlsx

In this article we work with xlsx files. The xlsx is a file extension for an   
open XML spreadsheet file format used by Microsoft Excel. The xlsm files support   
macros. The xls format is a proprietary binary format while xlsx is based on  
Office Open XML format.  

`pip install openpyxl`

We install openpyxl with the pip tool.

# Openpyxl create new file

In the first example, we create a new xlsx file with openpyxl.

```python
from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43

now = time.strftime("%x")
sheet['A3'] = now

book.save("sample.xlsx")
```

In the example, we create a new xlsx file. We write data into three cells.  


# Openpyxl write to a cell

There are two basic ways to write to a cell: using a key of a worksheet such as  
A1 or D3, or using a row and column notation with the cell method.

```python
from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 1
sheet.cell(row=2, column=2).value = 2

book.save('write2cell.xlsx')
```

In the example, we write two values to two cells.

```python
sheet['A1'] = 1
```

Here, we assing a numerical value to the A1 cell.


# Openpyxl append values

With the append method, we can append a group of values at the bottom of the  
current sheet.

```python
from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

book.save('appending.xlsx')
```

In the example, we append three columns of data into the current sheet.

```python
rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)
```

The data is stored in a tuple of tuples.

```python
for row in rows:
    sheet.append(row)
```

We go through the container row by row and insert the data row with the append method.  

# Openpyxl read cell

In the following example, we read the previously written data from the  
sample.xlsx file.

```python
import openpyxl

book = openpyxl.load_workbook('sample.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row=3, column=1)

print(a1.value)
print(a2.value)
print(a3.value)
```

# Openpyxl read multiple cells

We have the following data sheet:


# Openpyxl iterate by rows

The iter_rows function return cells from the worksheet as rows.

```python
from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=6, max_col=3):
    for cell in row:
        print(cell.value, end=" ")
    print()

book.save('iterbyrows.xlsx')
```

# Openpyxl iterate by columns

The iter_cols function returns cells from the worksheet as columns.

```python
from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

for row in sheet.iter_cols(min_row=1, min_col=1, max_row=6, max_col=3):
    for cell in row:
        print(cell.value, end=" ")
    print()

book.save('iterbycols.xlsx')
```

# Statistics

For the next example, we need to create a xlsx file containing numbers. For  
instance, we have created 25 rows of numbers in 10 columns with the `RANDBETWEEN`  
function.

```python
import openpyxl
import statistics as stats

book = openpyxl.load_workbook('numbers.xlsx', data_only=True)

sheet = book.active

rows = sheet.rows

values = []

for row in rows:
    for cell in row:
        values.append(cell.value)

print("Number of values: {0}".format(len(values)))
print("Sum of values: {0}".format(sum(values)))
print("Minimum value: {0}".format(min(values)))
print("Maximum value: {0}".format(max(values)))
print("Mean: {0}".format(stats.mean(values)))
print("Median: {0}".format(stats.median(values)))
print("Standard deviation: {0}".format(stats.stdev(values)))
print("Variance: {0}".format(stats.variance(values)))
```

# Openpyxl filter & sort data

A sheet has an auto_filter attribute, which allows to set filtering and sorting  
conditions.

Note that Openpyxl sets the conditions but we must apply them inside the  
Spreadsheet application.

```python
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

data = [
    ['Item', 'Colour'],
    ['pen', 'brown'],
    ['book', 'black'],
    ['plate', 'white'],
    ['chair', 'brown'],
    ['coin', 'gold'],
    ['bed', 'brown'],
    ['notebook', 'white'],
]

for r in data:
    sheet.append(r)

sheet.auto_filter.ref = 'A1:B8'
sheet.auto_filter.add_filter_column(1, ['brown', 'white'])
sheet.auto_filter.add_sort_condition('B2:B8')

wb.save('filtered.xlsx')
```

In the example, we create a sheet with items and their colours. We set a filter  
and a sort condition.


# Openpyxl dimensions

To get those cells that actually contain data, we can use dimensions.  

```python
from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A3'] = 39
sheet['B3'] = 19

rows = [
    (88, 46),
    (89, 38),
    (23, 59),
    (56, 21),
    (24, 18),
    (34, 15)
]

for row in rows:
    sheet.append(row)

print(sheet.dimensions)
print("Minimum row: {0}".format(sheet.min_row))
print("Maximum row: {0}".format(sheet.max_row))
print("Minimum column: {0}".format(sheet.min_column))
print("Maximum column: {0}".format(sheet.max_column))

for c1, c2 in sheet[sheet.dimensions]:
    print(c1.value, c2.value)

book.save('dimensions.xlsx')
```


# Sheets

Let's have a workbook with these three sheets.

```python
import openpyxl

book = openpyxl.load_workbook('sheets.xlsx')

print(book.get_sheet_names())

active_sheet = book.active
print(type(active_sheet))

sheet = book.get_sheet_by_name("March")
print(sheet.title)
```

The program works with Excel sheets.

```python
print(book.get_sheet_names())
```

The get_sheet_names method returns the names of available sheets in a workbook.

```python
active_sheet = book.active
print(type(active_sheet))
```

We get the active sheet and print its type to the terminal.

```python
sheet = book.get_sheet_by_name("March")
```

We get a reference to a sheet with the get_sheet_by_name method.

```python
print(sheet.title)
```

# Openpyxl Charts

The openpyxl library supports creation of various charts, including bar charts,  
line charts, area charts, bubble charts, scatter charts, and pie charts.  

According to the documentation, openpyxl supports chart creation within a worksheet   
only. Charts in existing workbooks will be lost.

```python
from openpyxl import Workbook
from openpyxl.chart import (
    Reference,
    Series,
    BarChart
)

book = Workbook()
sheet = book.active

rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("Germany", 11)
]

for row in rows:
    sheet.append(row)

data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=6)
categs = Reference(sheet, min_col=1, min_row=1, max_row=6)

chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categs)

chart.legend = None
chart.y_axis.majorGridlines = None
chart.varyColors = True
chart.title = "Olympic Gold medals in London"

sheet.add_chart(chart, "A8")

book.save("bar_chart.xlsx")
```

In the example, we create a bar chart to show the number of Olympic gold medals  
per country in London 2012.
