
from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def from_file(self, file):
    with open(file) as open_file:
      lines = open_file.readlines()
    for line in lines:
      if not len(line):
        continue

      item = line.strip().split(' ')
      if len(item) != 3:
        raise TypeError("Error with Line")
        
      node_from = item[0]
      node_to = item[1]
      distance = int(item[2])
      
      self.add_node(node_from)
      self.add_node(node_to)
      self.add_distance(node_from, node_to, distance)

    return self

  def add_node(self, value):
    self.nodes.add(value)

  def add_distance(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance

  def distance(self, from_node, to_node):
    return self.distances[from_node, to_node]

  def near_to(self, from_node, to_node):
    return to_node in self.edges[from_node]