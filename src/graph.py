class Edge:
  def __init__(self, destination):
    self.destination = destination

class Vertex:
  def __init__(self, value, color, **pos):   #TODO: test default arguments
    self.value = value
    self.color = color
    self.pos = pos
    self.edges = []

class Graph:
  def __init__(self):
    self.vertexes = []

  def create_test_data(self):
    vertex_1 = Vertex('V1', 'red', x=40, y=40)
    vertex_2 = Vertex('V2', 'blue', x=140, y=140)
    vertex_3 = Vertex('V3', 'green', x=220, y=250)
    vertex_4 = Vertex('V4', 'yellow', x=150, y=300)
    vertex_5 = Vertex('V5', 'purple', x=250, y=350)
    vertex_6 = Vertex('V6', 'cyan', x=350, y=275)
    vertex_7 = Vertex('V6', 'teal', x=350, y=400)

    vertex_1.edges.append(Edge(vertex_2))

    vertex_2.edges.append(Edge(vertex_3))
    vertex_2.edges.append(Edge(vertex_4))

    vertex_3.edges.append(Edge(vertex_4))

    vertex_4.edges.append(Edge(vertex_5))

    vertex_5.edges.append(Edge(vertex_6))
    vertex_5.edges.append(Edge(vertex_7))
    
    self.vertexes.extend([vertex_1, vertex_2, vertex_3, vertex_4, vertex_5, vertex_6, vertex_7])