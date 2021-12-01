import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import csv

# Load CSV file from DISASTER_USA_DETAILS folder
df = pd.read_csv('../DISASTER_USA_DETAILS/details_c.csv', quoting=csv.QUOTE_NONE, error_bad_lines=False,
                 warn_bad_lines=False)

print(df.shape)
# Getting the of number of cases grouped by event_type Column
new_df = df.groupby('event_id').count().reset_index()
new_df = new_df.rename(columns={'event_type': 'event_count'})

# Sorting event types
second_df = df.sort_values(by=['event_type'])

# Preparing data
data = [go.Bar(x=second_df['event_type'], y=new_df['event_count'])]

# Preparing layout
layout = go.Layout(title='The number of Each Type of Natural Disaster in the United States',
                   xaxis=dict(
                       title="Event Type",
                       type='category',
                       dtick=1,
                       showticklabels=True),
                   yaxis_title="Number of Disasters")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
