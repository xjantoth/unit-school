import pygal
import datetime
import random

# Define start and end dates for the range of dates to generate
start_date = datetime.datetime(2023, 1, 1, 0, 0)
end_date = datetime.datetime(2022, 12, 31, 23, 59)

# Generate a list of random datetimes
num_datetimes = 300
data = []
for i in range(num_datetimes):
    random_time = random.random()  # generates a random float between 0 and 1
    time_delta = (end_date - start_date) * random_time
    random_datetime = start_date + time_delta
    data.append((random_datetime, random.uniform(1, 50)))

# Create a line chart
line_chart = pygal.Line(x_label_rotation=40, interpolate='cubic', responsive=True)

# Set chart title
line_chart.title = 'Monthly Liquid Volume'

# Add x-axis labels
x_labels = [d.strftime('%H:%M:%S') for d, _ in data]
line_chart.x_labels = x_labels

# Add data to the chart
line_chart.add('Liquid Volume', [v for _, v in data])

# Render the chart
line_chart.render_to_file('liquid_volume.svg')
line_chart.render_in_browser()
