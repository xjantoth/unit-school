import pygal
import math

# Constants
radius = 5.0  # cm
height = 20.0  # cm
pi = math.pi

# Calculate the water volume for different levels
data = []
for level in range(0, 21):
    # Calculate the water volume using the formula for a frustum of a cone
    h = (height / 20.0) * level  # height of the water
    r = (radius / height) * h  # radius of the water surface
    volume = (1 / 3) * pi * h * (r**2 + r * radius + radius**2)
    data.append((level, volume))

# Create a line chart
line_chart = pygal.Line()

# Set the chart title
line_chart.title = 'Water Volume (cm^3)'

# Add the data to the chart
line_chart.add('Water Volume', [v for _, v in data])

# Set the x-axis labels
x_labels = [str(l) for l, _ in data]
line_chart.x_labels = x_labels

# Set the x-axis label
line_chart.x_title = 'Water Level (cm)'

# Set the y-axis label
line_chart.y_title = 'Volume (cm^3)'

# Render the chart to a file
line_chart.render_to_file('water_volume.svg')

