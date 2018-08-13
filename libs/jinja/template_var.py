#!/usr/bin/env python3

from jinja2 import Template

tm = Template("{% set name='Peter' -%} My name is {{ name }}")
msg = tm.render()

print(msg)
