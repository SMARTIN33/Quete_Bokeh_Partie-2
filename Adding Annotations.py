from bokeh.plotting import figure, show
from bokeh.models import Span, Label, LabelSet, BoxAnnotation

# Créez un graphique simple
p = figure(title="Graphique avec annotations", width=800, height=400)
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

# Ajout d'une ligne horizontale de repère
hline = Span(location=4, dimension='width', line_color='red', line_width=2)
p.add_layout(hline)

# Ajout d'une ligne verticale de repère
vline = Span(location=3, dimension='height', line_color='blue', line_width=2)
p.add_layout(vline)

# Ajout d'une étiquette
label = Label(x=3, y=4, text='Point Important', text_color='green', x_offset=5, y_offset=5)
p.add_layout(label)

# Ajout d'une boîte de mise en évidence
box = BoxAnnotation(left=1.5, right=3.5, fill_alpha=0.2, fill_color='lightgrey')
p.add_layout(box)

# Affichez le graphique
show(p)
