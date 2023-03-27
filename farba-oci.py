from pygal import Bar, Pie
from collections import defaultdict

preklad_farieb = {
    "hneda": "brown",
    "modra": "blue",
    "zelena": "green"
    }

chart = Bar()
#chart = Pie(inner_radius=0.5)
chart.title = 'Farba oci deti'

chart.y_title = 'Pocetnost farby oci'
chart.x_title = 'Farba'

data = {
    "Vilko": "hneda",
    "Simon": "modra",
    "Ema": "hneda",
    "Laura": "zelena",
    "Livka": "hneda",
    "Stelka": "zelena",
    "Peto": "modra",
    "Julka": "hneda",
    "Zuzka": "zelena",
    "Matus": "modra"
}


triedime = defaultdict(list)
for key, val in sorted(data.items()):
    triedime[val].append(key)


for key, value in triedime.items():
    chart.add(
            key, 
            [
                {'value': len(value), 
                 'label': ' '.join(value), 
                 'style': f'fill: {preklad_farieb.get(key, "black")};'
                 }
            ]
            )

chart.render_in_browser()
