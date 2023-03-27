#!/usr/bin/env python
from pygal import Line, Pie, Bar, style

# Hmotnost deti (skolaci) kg	
names = ['Vilko', 'Julka', 'Emka', 'Livka', 'Simon', 'Peto', 'Matus', 'Zuzka', 'Lukas', 'Stelka', 'Laura']
hmotnosti = [21.30, 37.20, 29.70, 27.70, 30.00, 35.80, 22.70, 54.60, 20.00, 24.50, 26.90]

# Hmotnost deti (skolka) kg	
names = ['Timi', 'Filip', 'Swenn', 'Ema', 'Zuzka', 'Tanicka', 'Beatka', 'Lubka', 'Alicka', 'Simi', 'Miska']
hmotnosti = [13.4, 12.9, 17.6, 20.6, 15.9, 16.4, 12.4, 20.7, 14.2, 11, 12]

#chart = Bar(
chart = Line(
        x_label_rotation=40, 
        show_legend=True, 
        style=style.DefaultStyle,
        interpolate='cubic',
        legend_at_bottom=True
        )

chart.title = 'Zobrazenie hmotnosti deti v Unit'
chart.y_title = 'Hmotnost [kg]'
chart.x_title = 'Folks'

priemerna_hmotnost = round(sum(hmotnosti) / len(hmotnosti), 2)

chart.x_labels = names
chart.add(None, 
          [{"label": "Hmotnost [kg]", "value": i} for i in hmotnosti],  
          )

chart.add(
        f'Priemerna hmotnost deti {priemerna_hmotnost} [kg]', 
        [priemerna_hmotnost for _ in range(len(hmotnosti))], 
        stroke_style={'width': 5, 'dasharray': '3, 6', 'linecap': 'round', 'linejoin': 'round'}
        )


chart.render_to_file('data/meranie_hmotnosti_deti_skolaci_line.svg')
chart.render_in_browser()

