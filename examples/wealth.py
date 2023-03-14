# Add data to the chart
from pygal import Bar
# Create a chart
chart = Bar()
chart.title = 'Wealth'

with open('data/gdp.csv') as f:
  for line in f:
    data = line.strip().split(',')
    chart.add(data[0], float(data[1]))

chart.render_in_browser()

