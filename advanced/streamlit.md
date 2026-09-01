# Streamlit 

Streamlit is an open-source Python library specifically designed for creating interactive and  
visually appealing web applications for machine learning and data science projects. It simplifies  
the process of turning data scripts into shareable web applications with minimal effort.

## Key Features
- **Ease of Use**: Streamlit is known for its simplicity and ease of use. You  
  can create web applications with just a few lines of Python code.  
- **Interactive Widgets**: It provides a variety of widgets (like sliders,  
  buttons, and text inputs) to create interactive applications.  
- **Real-time Updates**: Applications built with Streamlit can update in  
  real-time, which is especially useful for displaying dynamic data.  
- **Integration**: Streamlit integrates seamlessly with popular data science and  
  machine learning libraries such as Pandas, NumPy, Matplotlib, and  
  Scikit-learn.

## Common Uses
- *Data Visualization*: Creating interactive dashboards and visualizations to  
  explore and share data insights.  
- *Machine Learning*: Developing and sharing machine learning models with  
  real-time predictions.  
- *Exploratory Data Analysis (EDA)*: Building applications to interactively
  explore datasets.  
- *Prototyping*: Quickly prototyping data-driven applications without needing  
  extensive web development skills.  

## Dashboard

A *dashboard* is a graphical user interface (GUI) that displays key  
performance indicators (KPIs) and other relevant information at a glance. It  
consolidates and organizes data in a way that is easy to read, interpret, and  
interact with. Dashboards are used across various fields to monitor metrics,  
track progress, and make data-driven decisions.  

## Key Features

- *Visual Representation*: Dashboards use charts, graphs, and other visual  
  elements to represent data, making it easier to understand trends and  
  patterns.  
- *Real-time Data*: Many dashboards display real-time data, providing  
  up-to-date information for timely decision-making.  
- *Interactive Elements*: Users can often interact with dashboards through  
  filters, drill-downs, and other interactive features to explore data in more  
  detail.  
- *Customization*: Dashboards can be customized to show specific metrics and  
  KPIs relevant to the user or organization.  

## Common Uses

- *Business Intelligence*: Monitoring business metrics such as sales  
  performance, customer engagement, and financial health.  
- *Operations*: Tracking operational metrics like production efficiency,  
  inventory levels, and supply chain performance.  
- *Marketing*: Analyzing marketing campaign performance, website traffic, and  
  social media metrics.  
- *Healthcare*: Monitoring patient health metrics, hospital performance, and   
  resource utilization.  


## Reactivity

In Streamlit, *reactivity* refers to the application's ability to automatically update  
and display changes in real time based on user interactions, without the need for manual  
refreshes or reloading. When a user changes an input, such as entering text, adjusting  
a slider, or clicking a button, Streamlit immediately processes this change and updates  
the output dynamically. This feature enhances the interactivity and responsiveness  
of the application, creating a smooth user experience.


Streamlit appications are run with `streamlit run main.py`  


## Message

```python
import streamlit as st

st.write("My first streamlit application")
```

## Text input 

The example demonstrates the basic use of a text input widget combined with  
conditional content display. Streamlit's reactivity ensures that the app dynamically  
updates in real time. When you type your name into the text input box, Streamlit immediately  
reacts to this input and updates the display.

```python
import streamlit as st

st.title('Text input')

name = st.text_input('Enter your name:')

if name:
    st.write(f'Hello {name}!')
```

## Data table 

```python
import streamlit as st
import pandas as pd

df = pd.read_csv('products.csv')

# Display title and description
st.title('Data Dashboard')
st.write('This is a simple data dashboard using Streamlit.')

# use table to display data
st.table(df.head(15))
```

## Text input &  slider

```python
import streamlit as st

st.title('Text input and slider')

# Text input
name = st.text_input('Enter your name:')

# Slider
age = st.slider('Select your age:', 0, 100, 25)

# Button
if st.button('Submit'):
    st.write(f'Hello {name}, you are {age} years old!')
```

## Control number of rows with slider

```python
import streamlit as st
import pandas as pd

df = pd.read_csv('products.csv')

st.title('Data Dashboard')

# Set the default number of rows to display
default_rows = 10

# Create a slider to control the number of rows
n = st.slider("Number of rows to display", 3, len(df), value=default_rows)

# Display the DataFrame with the selected number of rows
st.table(df.head(n))
```

## Button 

Streamlit reruns the script from the beginning on every user interaction, such as clicking a button.  
The `st.write` method updates the displayed content based on the script's current state and conditions.  

```python
import streamlit as st

# Title of the app
st.title('Simple Button Example')

# Create a button
if st.button('Click Me'):
    st.write('Button clicked!')
else:
    st.write('Button not clicked.')
```

---

Random numbers 

```python
import streamlit as st
import numpy as np

st.title('Generate Random Numbers')

if st.button('Generate Random Numbers'):
    random_numbers = np.random.randint(0, 100, size=10)
    st.write('Random Numbers:', random_numbers)
else:
    st.write('Click to generate random numbers')
```


## Checkbox to show/hide dataframe

```python
import streamlit as st
import pandas as pd

st.title('Button to Display/Hide DataFrame')

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
}
df = pd.DataFrame(data)

# Create a toggle button to control visibility
show_df = st.checkbox('Show DataFrame')

# Display or hide the DataFrame based on the toggle state
if show_df:
    st.write(df)
```

## Select box

```python
import streamlit as st

st.write("Sidebar Example")
selection = st.selectbox('Choose a number:', [1, 2, 3, 4, 5])
st.write(f'Selected number: {selection}')
```



## Session state 

Session state in Streamlit allows you to store and access data across multiple  
reruns of your app. This is particularly useful for maintaining user preferences,  
tracking progress, or storing intermediate results.

Key Points:

- Persistence: The counter value is preserved across multiple reruns of the app, even  
  if the user refreshes the page or navigates to other parts of the app.
- Flexibility: You can store various data types in session state, including numbers,
  strings, lists, and dictionaries.

```python
import streamlit as st

# Initialize a counter in the session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Increment the counter and display it
if st.button('Increment'):
    st.session_state.counter += 1
    st.write(f'Counter: {st.session_state.counter}')
```

## Reruns

In Streamlit, a rerun refers to the process of re-executing the entire script or a  
specific fragment of it. This happens when a user interacts with a widget, such as   
clicking a button, changing a slider value, or entering text.  

Why Reruns Happen:

- User Interaction: When a user interacts with a widget, Streamlit detects the  
  change and triggers a rerun.
- Session State Updates: If you're using session state to store variables, changes  
  to these variables can also trigger a rerun.  
- Explicit Rerun: You can manually trigger a rerun using the `st.rerun()` function.



## Streamlit User Input and Reruns

Streamlit is a powerful Python library that allows you to create interactive  
web apps with minimal coding effort. It achieves this interactivity by continuously  
monitoring user input and rerunning the script whenever a change is detected.  

Here's a breakdown of how this process works:

1. *Initial Run:*
   - When you start your Streamlit app, the entire script is executed from top to bottom.  
   - Widgets are displayed on the web interface.

2. *User Interaction:*
   - *Widget Changes:* Whenever a user interacts with a widget (e.g., clicks a button,  
     changes a slider value, or enters text), Streamlit detects the change.  
   - *Event Trigger:* This change triggers an event, signaling the need for a rerun.  

3. *Rerun Process:*
   - **Full Rerun:** By default, the entire script is rerun from the beginning. This  
     ensures that all calculations, data processing, and widget updates are performed  
     based on the new input.
   - **Fragment Rerun:** For more efficient updates, Streamlit supports fragment reruns.  
     You can divide your app into fragments, each with its own set of widgets and logic.  
     When a widget within a fragment is changed, only that specific fragment is rerun,  
     optimizing performance.

Key Points:

- *State Preservation:* Streamlit maintains a session state, allowing you to store variables  
  and data between reruns. This enables you to preserve the app's state and avoid  
  unnecessary recalculations.  
- *Caching:* You can use Streamlit's caching mechanism to store the results of expensive  
  computations and avoid redundant calculations during reruns.  
- *Event Handlers:* While Streamlit's automatic rerunning is convenient, you can also define  
   custom event handlers using functions like `st.button` or `st.form` to trigger specific actions.  



## Line chart

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Line chart example')

# Generate random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Display line chart
st.line_chart(chart_data)
```

## Bar chart 

```python
import streamlit as st
import pandas as pd
import numpy as np

# Generate example data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Total Sales': [100, 150, 200, 250]
}

df = pd.DataFrame(data)

# Title of the app
st.title('Bar Chart Example')

# Display the bar chart
st.bar_chart(df.set_index('Category'))
```

## Area chart 

```python
import streamlit as st
import pandas as pd
import numpy as np

# Generate example data
data = np.random.randn(20, 3)
df = pd.DataFrame(data, columns=['a', 'b', 'c'])

# Display the area chart
st.area_chart(df)
```

## Map chart 

```python
import streamlit as st
import pandas as pd
import numpy as np

# Generate example data
data = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, 100),
    'lon': np.random.uniform(-180, 180, 100)
})

# Display the map
st.map(data)
```

## Histogram with Matplotlib

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate example data
data = np.random.randn(1000)

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor='black')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram Example')

# Display the chart using Streamlit
st.title('Histogram Example')
st.pyplot(fig)
```

## Scatter plot with Matplotlib

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate example data
x = np.random.rand(100)
y = np.random.rand(100)

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.scatter(x, y, c='blue', alpha=0.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Scatter Plot Example')

# Display the chart using Streamlit
st.title('Scatter Plot Example')
st.pyplot(fig)
```


## Pie chart with Plotly

```python
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generate example data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Quantity': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# Title of the app
st.title('Pie Chart Example')

# Create a pie chart
fig = px.pie(df, values='Quantity', names='Category', title='Quantity by Category')

# Display the pie chart using Streamlit
st.plotly_chart(fig)
```



## Upload a file

CSV file:  

```python
import streamlit as st
import pandas as pd

st.title('Upload CSV file')

# File uploader
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write('Uploaded DataFrame:')
    st.write(df)
```

---

```python
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("CSV File Loader and Exporter to Local PostgreSQL")

# Function to upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write("File uploaded successfully!")
    st.write(df)

    # Request database connection parameters
    st.sidebar.subheader("Database Connection Parameters")
    host = st.sidebar.text_input("Host", "localhost")
    database = st.sidebar.text_input("Database", "testdb")
    user = st.sidebar.text_input("User", "postgres")
    password = st.sidebar.text_input("Password", type="password")
    table_name = st.sidebar.text_input("Table Name", "Test")

    # Function to export DataFrame to PostgreSQL
    def export_to_postgresql(df, host, database, user, password, table_name):
        # Create the connection string
        engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')
        # Export DataFrame to PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)

    # Export the DataFrame to PostgreSQL
    if st.button("Export to PostgreSQL"):
        export_to_postgresql(df, host, database, user, password, table_name)
        st.write("Data exported to PostgreSQL successfully!")

else:
    st.write("No file uploaded.")
```



Excel file:  

```python
import streamlit as st
import pandas as pd

# Title of the app
st.title('Excel File Upload Example')

# File uploader
uploaded_file = st.file_uploader('Choose an Excel file', type=['xlsx', 'xls'])

if uploaded_file is not None:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file)
    
    # Display the DataFrame
    st.write('Uploaded Excel File Data:')
    st.write(df)
```


## Sidebar 

A sidebar is an optional component that provides a dedicated space on the side of  
the app's main content area for placing widgets, text, and other elements. This allows  
for better organization and easy access to controls and information, without cluttering  
the main interface. You can add elements to the sidebar using `st.sidebar`, which works  
similarly to the main st functions.

Using a sidebar helps keep your application clean and intuitive, ensuring a great user experience.  

```python
import streamlit as st

# Title of the app
st.title('Sidebar Widgets')

# Sidebar with a slider and text input
sidebar = st.sidebar
slider_value = sidebar.slider('Select a value:', 0, 100, 50)
text_input = sidebar.text_input('Enter a message:')

# Display the slider and text input values
st.write(f'Slider Value: {slider_value}')
st.write(f'Message: {text_input}')
```

## Two columns

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Two columns')

# Refresh button
if st.button('Refresh Data'):
    st.rerun()

# Create two columns
left_column, right_column = st.columns(2)

# Generate random data for the left column
dataframe = np.random.randn(10, 20)
left_column.dataframe(dataframe)

# Generate random data for the right column
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
right_column.line_chart(chart_data)
```

## Markdown

```python
import streamlit as st
import pandas as pd

# Title of the app
st.title('Streamlit markdown')

# Display a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
})

st.write('Simple DataFrame:')
st.write(df)

# Display some markdown text
st.markdown('This is **Streamlit**. You can write *markdown* too!')

st.markdown('Python *source code*')

st.markdown('''
~~~python
import streamlit as st
import pandas as pd

# Title of the app
st.title('Streamlit markdown')

# Display a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
})

st.write('Here is a simple DataFrame:')
st.write(df)

# Display some markdown text
st.markdown('This is **Streamlit**. You can write *markdown* too!')
~~~ ''')
```

## Interactive example

```python
import streamlit as st
import pandas as pd

st.title('Load CSV Data from URL')

# Create a text input box for the URL
csv_url = st.text_input('Enter the URL of a CSV file:')

# Create a button to load the data
if st.button('Load Data'):
    if csv_url:
        with st.spinner('Loading data...'):
            try:
                df = pd.read_csv(csv_url)
                st.session_state.df = df
                st.success('Data loaded successfully!')
            except Exception as e:
                st.error(f'Error loading data: {e}')
    else:
        st.warning('Please enter a valid URL.')

# Check if DataFrame is stored in session state
if 'df' in st.session_state:
    # Create a slider to control the number of rows displayed
    num_rows = st.slider('Select number of rows to display',
                          min_value=1,
                          max_value=len(st.session_state.df),
                          value=10,
                          key='num_rows_slider')

    # Display the DataFrame with the selected number of rows and specified width
    st.dataframe(st.session_state.df.head(num_rows), width=800)
```


## Database example

Inside a `.streamlit` directory in the `secrets.toml` file:

```toml
[connections.postgresql]
type="sql"
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "testdb"
username = "postgres"
password = "s$cret"
```


```python
import streamlit as st

con = st.connection("postgresql")
df = con.query("select * from cars")

st.dataframe(df)
```

---

```python
import streamlit as st

st.title("Car Data Explorer")

# Connect to the PostgreSQL database and store the DataFrame in session state
if 'df' not in st.session_state:
    with st.spinner('Connecting to database...'):
        try:
            con = st.connection("postgresql")
            st.session_state.df = con.query("SELECT * FROM cars")
            st.success("Database connection successful!")
        except Exception as e:
            st.error(f"Error connecting to database: {e}")

# Display the DataFrame
if 'df' in st.session_state:
    
    df = st.session_state.df
    st.dataframe(df)

    # Add interactive elements for filtering and sorting
    filter_column = st.selectbox('Filter by Column', df.columns)
    filter_value = st.text_input('Filter Value')

    if filter_value:
        filtered_df = df[df[filter_column] == filter_value]
        st.dataframe(filtered_df)

    # Add a simple line chart with car names on the x-axis
    st.subheader("Car Price Distribution")
    st.line_chart(df.set_index('name')['price'])
```

## Pages

```python
import streamlit as st
import pandas as pd
import numpy as np


def page1():
    st.title("Page 1: Random Data")
    df = pd.DataFrame(np.random.randn(10, 5), columns=[
                      'A', 'B', 'C', 'D', 'E'])
    st.dataframe(df)


def page2():
    st.title("Page 2: Emojis")
    st.write("Here are some emojis:")
    st.write(":smile:", ":heart:", ":joy:", ":heart_eyes:", ":cry:", 
             ":thumbsup:", ":thumbsdown:", ":raised_hands:", ":tada:",
             ":birthday:", ":dog:", ":sunglasses:", ":pleading_face:", ":shrug:", 
             ":sparkles:", ":pizza:", ":star2:", ":books:", ":art:")


def page3():
    st.title("Page 3: Lorem Ipsum")
    st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
""")


page_names = ["Random Data", "Emojis", "Lorem Ipsum"]
selected_page = st.sidebar.selectbox("Select a Page", page_names)

if selected_page == "Random Data":
    page1()
elif selected_page == "Emojis":
    page2()
else:
    page3()
```


## Multi page app with configuration

Directory structure:

```
.streamlit\
  config.toml
pages\
  Emojis.py
  Lorem_Ipsum.py
  Random_Numbers.py
app.py
```


In `.streamlit/config.toml`: 

```toml
[theme]
primaryColor = "#cb7a00"
backgroundColor = "#25282A"
secondaryBackgroundColor = "#155557"
textColor = "#ffffff"
font = "sans serif"
```



The `app.py` file:  

```python
import streamlit as st

# Automatically loads pages from the 'pages' directory
st.title("Multi-Page App")
```

The `Lorem_Ipsum.py` file:  

```python
import streamlit as st

st.title("Page 3: Lorem Ipsum")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
""")
```

The `Emojis.py` file:  

```python
import streamlit as st

st.title("Emojis")

st.write("Here are some emojis:")
st.write(":smile:", ":heart:", ":joy:", ":heart_eyes:", ":cry:", 
         ":thumbsup:", ":thumbsdown:", ":raised_hands:", ":tada:",
         ":birthday:", ":dog:", ":sunglasses:", ":pleading_face:", ":shrug:", 
         ":sparkles:", ":pizza:", ":star2:", ":books:", ":art:")
```


The `Random_Numbers.py` file:  

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Random numbers")

df = pd.DataFrame(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
st.dataframe(df)
```
