# Add data to the chart
from pygal import Bar
# Create a chart
chart = Bar()
chart.title = 'Population'

with open('data/pop.csv') as f:
  for line in f:
    data = line.strip().split(',')
    chart.add(data[0], int(data[1]))

chart.render_in_browser()

