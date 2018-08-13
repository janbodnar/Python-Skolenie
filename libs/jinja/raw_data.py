#!/usr/bin/env python3

from jinja2 import Template

data = '''
{% raw -%}
His name is {{ name -}}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='Peter')

print(msg)
