import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
  color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=30, width=38, fill_color='color')

# this is drawing the edges from start to end
graph.edge_renderer.data_source.data = dict(start=[], end=[])
    # start=[i for i, vertex in enumerate(graph_data.vertexes)],  # this is why all edges start from first vertex, a list that has to do with starting points
    # end=[edge for vertex in graph_data.vertexes.edges) # a list of some kind that has to do with ending points
    # end=[1, 2, 3, 4]) # a list of some kind that has to do with ending points

for vertex in graph_data.vertexes:
  if len(vertex.edges) > 0:
    for edge in vertex.edges:
      start = graph_data.vertexes.index(vertex)
      graph.edge_renderer.data_source.data['start'].append(start)

      end = graph_data.vertexes.index(edge.destination)
      graph.edge_renderer.data_source.data['end'].append(end)


print(graph.edge_renderer.data_source.data)

### start of layout code
# looks like this is setting positions of the vertexes
circ = [i*2*math.pi/N for i in node_indices]
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

source = ColumnDataSource(data=dict(x_pos=x,
                                    y_pos=y,
                                    names=['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']))

labels = LabelSet(x='x_pos', y='y_pos', text='names', level='glyph',
              x_offset=-10, y_offset=-10, source=source, render_mode='canvas')


graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

plot.add_layout(labels)

output_file('graph.html')
show(plot)