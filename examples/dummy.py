import pygal

# create a chart
chart = pygal.Line()

# add data to the chart
chart.add('Data 1', [1, 3, 5, 7, 9], tooltip=[('Data 1', 'Value: {0:.2f}'), None, None, None, None])
chart.add('Data 2', [2, 4, 6, 8, 10])

# render the chart
chart.render_in_browser()
