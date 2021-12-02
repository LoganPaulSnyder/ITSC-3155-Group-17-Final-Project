import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import csv

# Load CSV file from DISASTER_USA_DETAILS folder
df = pd.read_csv('../DISASTER_USA_DETAILS/fatalities_c.csv', error_bad_lines=False,
                 warn_bad_lines=False)

df = df.sort_values(by=['fatality_date'])

data = [go.Scatter(x=df['fatality_date'], y=df['fatality_location'], mode='markers')]

# Preparing layout
layout = go.Layout(title='Fatalities in July 2021',
                   xaxis_title="Date of Fatality",
                   yaxis_title="Location of Fatality")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')
