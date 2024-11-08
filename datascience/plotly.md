# Plotly

Plotly is a powerful open-source graphing library that enables the creation of high-quality,  
interactive visualizations in Python, R, JavaScript, and other programming languages.  
It's particularly popular for its ease of use and flexibility, making it a favorite among   
data scientists, analysts, and developers.

Key Features:
- Interactive Plots: Allows users to create interactive graphs and charts, which can be  
  embedded in web applications, Jupyter notebooks, and dashboards.  
- Wide Range of Charts: Supports a variety of chart types, including line charts, scatter   
  plots, bar charts, heatmaps, 3D plots, and more.  
- Customization: Offers extensive customization options to tailor plots to specific needs,  
  including custom layouts, annotations, and styles.  
- Integration: Easily integrates with other tools and libraries, such as Dash for building  
  interactive web applications, and can be used with frameworks like Flask and Django. 
- Free and Open Source: While Plotly provides premium services, the core graphing libraries 
- are open-source and freely available. 

## Simple line chart

```python
import plotly.express as px

# Sample data
df = px.data.gapminder().query("country=='Canada'")

# Create a line chart
fig = px.line(df, x='year', y='gdpPercap', title='GDP per Capita in Canada')

# Show the plot
fig.show()
```

## Bar chart

```python
import plotly.express as px

# Sample data
data = {
    'Country': ['USA', 'China', 'Russia', 'Germany', 'Japan'],
    'Gold': [39, 38, 25, 23, 27],
    'Silver': [41, 32, 28, 26, 14],
    'Bronze': [33, 18, 23, 23, 17]
}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_long = df.melt(id_vars='Country', var_name='Medal', value_name='Count')

# Create a bar chart
fig = px.bar(df_long, x='Country', y='Count', color='Medal', title='Medals Won by Country')

# Show the plot
fig.show()
```

```python
from flask import Flask, render_template_string
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = {
        'Country': ['USA', 'China', 'Russia', 'Germany', 'Japan'],
        'Gold': [39, 38, 25, 23, 27],
        'Silver': [41, 32, 28, 26, 14],
        'Bronze': [33, 18, 23, 23, 17]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Melt the DataFrame to long format
    df_long = df.melt(id_vars='Country', var_name='Medal', value_name='Count')

    # Create a bar chart
    fig = px.bar(df_long, x='Country', y='Count', color='Medal', title='Medals Won by Country')

    # Convert the plotly figure to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the plot in HTML
    return render_template_string("""
    <html>
    <head>
        <title>Plotly Flask App</title>
    </head>
    <body>
        <h1>Plotly Bar Chart in Flask</h1>
        <div>{{ plot | safe }}</div>
    </body>
    </html>
    """, plot=plot_html)

if __name__ == '__main__':
    app.run(debug=True)
```


## Scatter with plotly


```python
from flask import Flask, render_template_string
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    df = px.data.iris()

    # Create a plotly figure
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                     title='Sepal Width vs Sepal Length')

    # Convert the plotly figure to HTML
    plot_html = fig.to_html(full_html=False)

    # Render the plot in HTML
    return render_template_string("""
    <html>
    <head>
        <title>Plotly Flask App</title>
    </head>
    <body>
        <h1>Plotly Plot in Flask</h1>
        <div>{{ plot | safe }}</div>
    </body>
    </html>
    """, plot=plot_html)

if __name__ == '__main__':
    app.run(debug=True)

```
