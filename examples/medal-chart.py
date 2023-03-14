# Add data to the chart
from pygal import Bar
from pygal.style import LightSolarizedStyle

# Create a chart
chart = Bar(style=LightSolarizedStyle)
chart.title = 'Olympic medals'

with open('data/medals.csv') as f:
  for line in f:
    data = line.strip().split(',')
    chart.add(data[0], int(data[1]))

chart.render_in_browser()
