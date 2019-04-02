# -*- coding:utf-8 -*-

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotattion=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 40491, 'label': 'Description of httpie.'},
    {'value': 40495, 'label': 'Description of django.'},
    {'value': 43000, 'label': 'Description of flask.'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
