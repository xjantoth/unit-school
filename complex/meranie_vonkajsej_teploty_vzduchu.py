#!/usr/bin/env python
import random
import datetime
from pygal import Line, Pie, Bar, style

# Vygenerujem si cas a nameranu hodnotu vzduchu
start = datetime.datetime.today()
merania = [(start, random.uniform(1, 20))]

for i in range(20):
    next_date = merania[-1][0] +  datetime.timedelta(minutes=random.randint(10, 70))
    merania.append((next_date, random.uniform(1, 20)))


# Create Bar chart
chart = Bar(x_label_rotation=40, show_legend=False, style=style.LightSolarizedStyle) 
chart.title = 'Meranie vonkajšej teploty vzduchu (°C)'
chart.y_title = 'Teplota [°C]'
chart.x_title = 'Čas merania'

x_labels = [d.strftime('%Y-%m-%d %H:%M:%S') for d, _ in merania]
chart.x_labels = x_labels

# Add data to the chart
chart.add('Meranie teploty °C', [v for _, v in merania])

chart.render_to_file('meranie_vonkajsej_teploty_vzduchu_bar.svg')


# Create Line chart
chart = Line(x_label_rotation=40, show_legend=False , style=style.LightSolarizedStyle)
chart.title = 'Meranie vonkajšej teploty vzduchu (°C)'
chart.y_title = 'Teplota [°C]'
chart.x_title = 'Čas merania'

x_labels = [d.strftime('%Y-%m-%d %H:%M:%S') for d, _ in merania]
chart.x_labels = x_labels

# Add data to the chart
chart.add('Meranie teploty °C', [v for _, v in merania])

chart.render_to_file('meranie_vonkajsej_teploty_vzduchu_line.svg')
chart.render_in_browser()

