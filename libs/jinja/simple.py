#!/usr/bin/env python3

from jinja2 import Template

tm = Template("My name is {{ name }}")
msg = tm.render(name="Peter")

print(msg)
