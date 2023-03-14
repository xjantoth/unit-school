from pygal import Pie

chart = Pie()
chart.title = 'Carbon Dioxide'

with open('data/carbon.csv') as f:
  for line in f:
    data = line.strip().split(',')
    chart.add(data[0], float(data[1]))

chart.render_in_browser()
