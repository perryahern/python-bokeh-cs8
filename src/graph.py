from random import randint
import random

class Edge:
  def __init__(self, destination):
    self.destination = destination

class Vertex:
  def __init__(self, value, **pos):   #TODO: test default arguments
    self.value = value
    self.color = 'white'
    self.pos = pos
    self.edges = []

class Graph:
  def __init__(self):
    self.vertexes = []

  def create_test_data(self):
    vertex_1 = Vertex('t1', x=40, y=40)
    vertex_2 = Vertex('t2', x=140, y=140)
    vertex_3 = Vertex('t3', x=220, y=250)
    vertex_4 = Vertex('t4', x=150, y=300)
    vertex_5 = Vertex('t5', x=250, y=350)
    vertex_6 = Vertex('t6', x=350, y=275)
    vertex_7 = Vertex('t7', x=350, y=400)
    vertex_8 = Vertex('t8', x=400, y=425)
    vertex_9 = Vertex('t9', x=425, y=375)
    vertex_10 = Vertex('t10', x=450, y=325)
    vertex_11 = Vertex('t11', x=300, y=100)
    vertex_12 = Vertex('t12', x=350, y=150)

    vertex_1.edges.append(Edge(vertex_2))

    vertex_2.edges.append(Edge(vertex_3))
    vertex_2.edges.append(Edge(vertex_4))

    vertex_3.edges.append(Edge(vertex_4))

    vertex_4.edges.append(Edge(vertex_5))

    vertex_5.edges.append(Edge(vertex_6))
    vertex_5.edges.append(Edge(vertex_7))

    vertex_8.edges.append(Edge(vertex_9))
    vertex_9.edges.append(Edge(vertex_10))

    vertex_11.edges.append(Edge(vertex_12))
    
    
    self.vertexes.extend([vertex_1, vertex_2, vertex_3, vertex_4, vertex_5,
                          vertex_6, vertex_7, vertex_8, vertex_9, vertex_10, vertex_11, vertex_12])

  def randomize(self, width, height, pxBox, probability=0.6):
    def connectVerts(v0, v1):
      v0.edges.append(Edge(v1))
      v1.edges.append(Edge(v0))
  
    count = 0

    grid = []
    for y in range(height):
      row = []
      for x in range(width):
        value = 't' + str(count)
        count += 1
        v = Vertex(value)
        row.append(v)
      grid.append(row)
    
    for y in range(height):
      for x in range(width):
        #connect down
        if y < height -1:
          if randint(0, 1) < probability:
            connectVerts(grid[y][x], grid[y+1][x])

        #connect right
        if x < width -1:
          if randint(0, 1) < probability:
            connectVerts(grid[y][x], grid[y][x+1])
  
    boxBuffer = 0.5
    boxInner = pxBox * boxBuffer
    boxInnerOffset = (pxBox - boxInner) / 2

    for y in range(height):
      for x in range(width):
        grid[y][x].pos = {
          'x': (x * pxBox + boxInnerOffset + randint(0, 1) * boxInner),
          'y': (y * pxBox + boxInnerOffset + randint(0, 1) * boxInner) 
        }
    
    for y in range(height):
      for x in range(width):
        self.vertexes.append(grid[y][x])

  
  def bfs(self, start):
    queue = [start]
    found = [start]

    start.color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    while len(queue) > 0:
      v = queue[0]
      for edge in v.edges:
        if edge.destination not in found:
          found.append(edge.destination)
          queue.append(edge.destination)
          edge.destination.color = start.color
      queue.pop(0)  # TODO: Look at collections.dequeue
    return found

  def get_connected_components(self):
    searched = []
    for vertex in self.vertexes:
      if vertex not in searched:
        searched = searched + [vertex] + self.bfs(vertex)
