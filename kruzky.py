#!/usr/bin/env python
from pygal import Line, Pie, Bar, style


names = ['Vilko','Julka','Emka','Livka','Simon','Peto','Matus','Zuzka','Ja','Stelka']
kruzky = [3, 3, 4, 1, 5, 1, 3, 1, 2, 2]


chart = Line(
        x_label_rotation=40, 
        show_legend=True, 
        style=style.DefaultStyle,
        interpolate='cubic',
        legend_at_bottom=True
        )

chart.title = 'Zobrazenie poctu kruzkov deti v Unit'
chart.y_title = 'Pocet kruzkov'
chart.x_title = 'Folks'

priemer_kruzkov = round(sum(kruzky) / len(kruzky), 2)

chart.x_labels = names
chart.add(None, [{"label": "Pocet kruzkov", "value": i} for i in kruzky])

chart.add(
        f'Priemerny pocet kruzkov {priemer_kruzkov}', 
        [priemer_kruzkov for _ in range(len(kruzky))], 
        color='gray'
        )


chart.render_to_file('data/pocet_kruzkov_deti_skolaci_line.svg')
chart.render_in_browser()


# # Kolacovy graf
pie_chart = Pie()
pie_chart.title = 'Pocet kruzkov deti v Unit school'
#pie_chart.y_title = 'Hmotnost [kg]'
pie_chart.x_title = 'Folks'

for meno, hm in zip(names, kruzky):
    pie_chart.add(meno, hm)
    print(meno, hm)

pie_chart.render_to_file('data/proce_kruzkov_deti_skolaci_pie.svg')
pie_chart.render_in_browser()


