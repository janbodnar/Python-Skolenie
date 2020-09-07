#!/usr/bin/python

from pathlib import Path
import datetime
from prettytable import PrettyTable

path = Path('C:/Users/Jano/Documents/')

pt = PrettyTable()
pt.field_names = ["File name", "Size", "Created"]

pt.align["File name"] = "l"
pt.align["Size"] = "r"
pt.align["Created"] = "l"

for e in path.glob('**/*.txt'):

    created = datetime.datetime.fromtimestamp(e.stat().st_ctime)
    size = e.stat().st_size
    pt.add_row([e.name, size, f"{created:%Y-%m-%d}"])
    
print(pt)
