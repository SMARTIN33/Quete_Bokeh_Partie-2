from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import row

# Données partagées
source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5]))

# Créez le premier graphique avec un cercle
p1 = figure(title="Graphique avec plages et sélections liées", width=400, height=400)
p1.circle('x', 'y', source=source, size=10, color="navy", alpha=0.6)

# Créez le deuxième graphique avec une ligne et des plages liées
p2 = figure(title="Graphique lié", width=400, height=400, x_range=p1.x_range, y_range=p1.y_range)
p2.line('x', 'y', source=source, line_width=2, color="orange")

# Ajouter l'outil de survol au premier graphique
hover = HoverTool(tooltips=[("X", "$x"), ("Y", "$y")])
p1.add_tools(hover)

# Affichez les graphiques en disposition de rangée
show(row(p1, p2))
