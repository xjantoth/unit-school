#Mesiac narodenia (Petko)	
from pygal import Bar, Pie
from collections import defaultdict

chart = Bar()
chart = Pie(inner_radius=0.6)
chart.title = 'Mesiac narodenia deti'

chart.y_title = 'Pocetnost deti nardenych v mesiaci'
chart.x_title = 'Mesiac v kalendarnom roku'

data = {
    "Petko": "Januar",
    "Vilko": "Marec",
    "Zuzka": "September",
    "Simon": "Januar",
    "Matus": "Oktober",
    "Stelka": "November",
    "Ema": "November",
    "Julka": "April",
    "Laura": "Marec",
    "Livka": "Februar"
    }


triedime = defaultdict(list)
for key, val in sorted(data.items()):
    triedime[val].append(key)


for key, value in triedime.items():
    chart.add(key, [{'value': len(value), 'label': ' '.join(value)}])

chart.render_in_browser()
