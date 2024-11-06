# The panel library

The Panel library is an open-source Python library designed to streamline the development  
of robust tools, dashboards, and complex applications entirely within Python. It is part of  
the HoloViz ecosystem, which provides a suite of data exploration tools.

```
pip install panel
```

```
panel serve app.py
```

Main use cases:  

- Dashboards - Create interactive and dynamic dashboards to visualize and  
  explore data.
- Web Applications - Develop web applications with user interfaces that interact  
  with Python code.
- Exploratory Data Analysis - Build tools to quickly explore and analyze data  
  sets interactively.
- Interactive Reports - Generate interactive reports that allow users to  
  manipulate data and visualize results.
- Real-Time Monitoring - Set up real-time monitoring dashboards to track live  
  data feeds and visualize changes.
- Custom GUIs - Create custom graphical user interfaces for scientific  
  computing, financial analysis, and other applications.


## Simple 

```python
import panel as pn

pn.extension()

pn.panel("Panel 1").servable()
pn.panel("Panel 2").servable()
pn.panel("Panel 3").servable()
```

## Slider

```python
import panel as pn

# Initialize the Panel extension
pn.extension()

# Create a FloatSlider widget
slider = pn.widgets.FloatSlider(name='Value', start=0, end=10, step=0.1)

# Bind the slider value to a text display
text = pn.bind(lambda x: f"Slider value: {x:.1f}", slider)

# Create a layout with the slider and text display
app = pn.Column(slider, text)

# Display the app
app.show()
```

## Rows

```python
import panel as pn

#  Apply the custom CSS

custom_css = """
* {
    background-color: #2e2e2e;
    color: white;
}
"""

# Apply the custom CSS
pn.extension(raw_css=[custom_css])

# # Create a Panel object
# text = pn.pane.Markdown("## This is some text on a dark background")

# # Display the Panel
# pn.Row(text).show()


component1 = pn.panel("Panel 1")
component2 = pn.panel("Panel 2")

base = pn.FlexBox(flex_direction='column')

row1 = pn.Row(
    component1, component2,
    pn.pane.HTML("<p>paragraph</p>"),
    pn.pane.Str(
        'This is a raw string that will not be formatted in any way.',
    )
)

row2 = pn.Row(
    pn.pane.Markdown("""\
# Wind Turbine

A wind turbine is a device that converts the kinetic energy of wind into \
[electrical energy](https://en.wikipedia.org/wiki/Electrical_energy).

Read more [here](https://en.wikipedia.org/wiki/Wind_turbine).
""")
)

base.append(row1)
base.append(row2)

print(base)
base.servable()
```

## Dataframe

```python
import pandas as pd
import panel as pn

pn.extension()

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

table = pn.widgets.DataFrame(df, name='DataFrame Viewer')
table.width = 400
table.height = 350

app = pn.Column("# DataFrame Viewer", table)
app.show()
```


## Matplotlib example

```python
import panel as pn
import matplotlib.pyplot as plt
import numpy as np

pn.extension()

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plot = pn.pane.Matplotlib(plt.gcf(), tight=True)

app = pn.Column("# Simple Sine Wave Plot", plot)
app.show()
```






