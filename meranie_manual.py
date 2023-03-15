#!/usr/bin/env python
import random
from pygal import Line, Pie, Bar, style
from pygal.style import Style

custom_style = Style(
  background='transparent',
  plot_background='transparent',
  #foreground='#53EBBB',
  #foreground_strong='#53B0E8',
  #foreground_subtle='#631C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#5A1A25', '#E8537A', '#0000FF', '#0000FF'))

# Create Bar chart
chart = Line(
        x_label_rotation=40, 
        show_legend=True, 
        #style=style.LightSolarizedStyle,
        style=custom_style,
        interpolate='cubic',
        legend_at_bottom=True
        )

chart.title = 'Meranie teploty vzduchu (°C)'
chart.y_title = 'Teplota [°C]'
chart.x_title = 'Čas merania'

x_labels = [
        '2023-03-15 13:17:23', 
        '2023-03-15 13:58:23', 
        '2023-03-15 14:55:23', 
        '2023-03-15 15:05:23', 
        '2023-03-15 16:11:23', 
        '2023-03-15 17:06:23', 
        '2023-03-15 17:40:23', 
        '2023-03-15 18:08:23', 
        '2023-03-15 18:41:23', 
        '2023-03-15 19:38:23', 
        '2023-03-15 19:51:23'
        ]

meranie_vonku = [4, 3.61, 6.13, 4.49, 4.94, 2.94, 1.34, 3.57, 4.42, 5.38, 4.54]

meranie_vnutorna = [i + 18 for i in meranie_vonku]
random.shuffle(meranie_vnutorna)

priemer_tmp_vonku = round(sum(meranie_vonku) / len(meranie_vonku), 1)
priemer_tmp_vnutorna = round(sum(meranie_vnutorna) / len(meranie_vnutorna), 1)  

chart.x_labels = x_labels

# Add data to the chart
chart.add(f'Outside tmp - avg: {priemer_tmp_vonku} [°C]', meranie_vonku)
chart.add(f'Inside tmp - avg: {priemer_tmp_vnutorna} [°C]', meranie_vnutorna)

chart.add(None, [priemer_tmp_vonku for _ in range(len(meranie_vonku))], color='gray')
chart.add(None, [priemer_tmp_vnutorna for _ in range(len(meranie_vnutorna))], color='gray')


chart.render_to_file('meranie_manual.svg')
#chart.render_in_browser()

