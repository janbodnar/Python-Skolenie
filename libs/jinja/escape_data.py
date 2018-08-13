#!/usr/bin/env python3

from jinja2 import Template, escape

data = '<a>Today is a sunny day</a>'

# e = Environment(loader=fileloader, autoescape=True)
tm = Template("{{ data | e}}")
msg = tm.render(data=data)

print(msg)
print(escape(data))
