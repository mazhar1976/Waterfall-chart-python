# Imports
import plotly.graph_objects as go
import plotly
import pandas as pd
import sys
import os
os.chdir(sys.path[0])

# Read Excel Data and store it in a variable: df [dataframe]
df = pd.read_excel('data.xlsx')

# Store values of columns in a seperate variable
x = df['Category']
y = df['Actuals']
y2 = df['Forecast']
measure = df['Measure']
text = df['Text']

# Create Waterfall Chart
fig = go.Figure()

# Add First Trace
fig.add_trace(go.Waterfall(
        measure = measure,
        x = x,
        y = y,
        text = text,
        textposition = 'outside',
        name="Actuals"
))

# Add Second Trace
fig.add_trace(go.Waterfall(
        measure = measure,
        x = x,
        y = y2,
        text = text,
        textposition = 'outside',
        name="Forecast"
))

# Update Layout [OPTIONAL]
# Layout Options: https://plotly.com/python/reference/layout/#layout-waterfallgroupgap
fig.update_layout(
        title = 'EBIT Development 2018 - 2020 in mio USD',
        title_font_size = 32,
        waterfallgroupgap=0.3, # Value between 0-1
        waterfallmode='group', # Group or Overlay
        font_size = 16,
        plot_bgcolor = 'rgba(0,0,0,0)' # Transparent Background
)

# Export Waterfall to HTML
plotly.offline.plot(fig,filename='Waterfall.html')
