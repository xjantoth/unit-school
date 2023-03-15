import pygal
from datetime import datetime, timedelta

# Example data
data = [
    {'timestamp': datetime(2023, 3, 1, 0, 0), 'temperature': 20},
    {'timestamp': datetime(2023, 3, 2, 0, 0), 'temperature': 22},
    {'timestamp': datetime(2023, 3, 3, 0, 0), 'temperature': 18},
    {'timestamp': datetime(2023, 3, 4, 0, 0), 'temperature': 19},
    {'timestamp': datetime(2023, 3, 5, 0, 0), 'temperature': 23},
    {'timestamp': datetime(2023, 3, 6, 0, 0), 'temperature': 21},
    {'timestamp': datetime(2023, 3, 7, 0, 0), 'temperature': 20},
]

# Calculate the average temperature
avg_temp = sum([item['temperature'] for item in data])/len(data)

# Create a line chart
line_chart = pygal.Line()

# Add the temperature data
line_chart.add('Temperature', [(item['timestamp'], item['temperature']) for item in data])

# Add the average temperature line
line_chart.add('Average Temperature', [(data[0]['timestamp'], avg_temp), (data[-1]['timestamp'], avg_temp)])

# Render the chart
line_chart.render_in_browser()

