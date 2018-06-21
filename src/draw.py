import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

WIDTH = 640   # TODO: Currently gaph renders square, scaled to these numbers
HEIGHT = 480  # TODO: Check for solutions (possible: https://stackoverflow.com/questions/21980662/how-to-change-size-of-bokeh-figure)
CIRCLE_SIZE = 30


graph_data = Graph()
# graph_data.create_test_data()
graph_data.randomize(4, 3, 150, 0.6)

N = len(graph_data.vertexes)
node_indices = list(range(N))
graph_data.get_connected_components()

color_list = []
for vertex in graph_data.vertexes:
  color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, WIDTH), y_range=(0, HEIGHT),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')

# this is drawing the edges from start to end
graph.edge_renderer.data_source.data = dict(start=[], end=[])

for vertex in graph_data.vertexes:
  for edge in vertex.edges:
    start = graph_data.vertexes.index(vertex)
    graph.edge_renderer.data_source.data['start'].append(start)

    end = graph_data.vertexes.index(edge.destination)
    graph.edge_renderer.data_source.data['end'].append(end)


### start of layout code
circ = [i*2*math.pi/N for i in node_indices]
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]
values = [v.value for v in graph_data.vertexes]

# Draw the labels
source = ColumnDataSource(data=dict(x=x, y=y, values=values))
labels = LabelSet(x='x', y='y', text='values', level='overlay',
                  text_align='center', text_baseline='middle', source=source, render_mode='canvas')
plot.add_layout(labels)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)