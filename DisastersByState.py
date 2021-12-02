import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import csv

# Load CSV file from DISASTER_USA_DETAILS folder
df = pd.read_csv('../DISASTER_USA_DETAILS/details_c.csv', quoting=csv.QUOTE_NONE, error_bad_lines=False,
                 warn_bad_lines=False)

# Getting the of number of cases grouped by state and event_type Columns
new_df = df.groupby('state').count().reset_index()

# Preparing data
data = [go.Bar(x=new_df['state'], y=new_df['event_type'])]

# Preparing layout
layout = go.Layout(title='Natural Disasters in July 2021 for Each State',
                   xaxis=dict(
                       title="State",
                       type='category',
                       dtick=1,
                       showticklabels=True),
                   yaxis=dict(
                       title="Number of Disasters",
                        range=[0, 100]))

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart2.html')