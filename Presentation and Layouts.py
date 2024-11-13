from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot

# Créez quelques graphiques simples
p1 = figure(title="Graphique 1")
p1.line([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], line_width=2)

p2 = figure(title="Graphique 2")
p2.circle([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], size=10, color="navy", alpha=0.5)

p3 = figure(title="Graphique 3")
p3.line([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], line_color="orange", line_width=2)

# Organiser les graphiques en rangée
layout_row = row(p1, p2)

# Organiser les graphiques en colonne
layout_column = column(p1, p3)

# Créer une grille avec les graphiques
layout_grid = gridplot([[p1, p2], [None, p3]])  # None crée un espace vide

# Affichez les différentes mises en page
show(layout_row)
show(layout_column)
show(layout_grid)
