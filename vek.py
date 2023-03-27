#!/usr/bin/env python
from pygal import Line, Pie, Bar, style

names = ['Vilko', 'Julka', 'Emka', 'Livka', 'Simon', 'Peto', 'Matus', 'Zuzka', 'Lukas']
vek = [6, 10, 10, 12, 10, 8, 7, 1, 5]

chart = Line(
        x_label_rotation=40, 
        show_legend=True, 
        style=style.DefaultStyle,
        interpolate='cubic',
        legend_at_bottom=True
        )

chart.title = 'Zobrazenie veku deti v Unit'
chart.y_title = ' Vek'
chart.x_title = 'Folks'

priemer_vek = round(sum(vek) / len(vek), 2)

chart.x_labels = names
chart.add(None, [{"label": " Vek", "value": i} for i in vek])

chart.add(
        f'Priemerny  vek {priemer_vek}', 
        [priemer_vek for _ in range(len(vek))], 
        color='gray'
        )


chart.render_to_file('data/vek_deti_skolaci_line.svg')
chart.render_in_browser()


# # # Kolacovy graf
# pie_chart = Pie()
# pie_chart.title = 'Zobrazenie veku deti v Unit school'
# pie_chart.x_title = 'Folks'
#
# for meno, hm in zip(names, vek):
#     pie_chart.add(meno, hm)
#     print(meno, hm)
#
# pie_chart.render_to_file('data/vek_deti_skolaci_pie.svg')
# pie_chart.render_in_browser()


