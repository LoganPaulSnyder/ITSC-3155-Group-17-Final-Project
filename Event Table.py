import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import csv

# Load CSV file from DISASTER_USA_DETAILS folder
df = pd.read_csv('../DISASTER_USA_DETAILS/details_c.csv', error_bad_lines=False,
                 warn_bad_lines=False)

#Sort the table by state
df = df.sort_values(by=['state'])

#Create DataTable
data = go.Figure(data=[go.Table(
    columnwidth = [80,80, 400],
    header=dict(values=["State", "Event", "Description"],
                fill_color='lightgreen',
                line_color='black',
                font_size=20,
                align='center'),
    cells=dict(values=[df.state, df.event_type, df.event_narrative],
               fill_color='white',
               line_color='black',
               align='left',
               height=50))
])

# Plot the figure and saving in a html file
fig = go.Figure(data=data)
pyo.plot(fig, filename='Table.html')