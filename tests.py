import unittest

from classes import Graph
from functions import *

class GraphTest(unittest.TestCase):

  def setUp(self):
    self.g = Graph()
    self.g.add_node("A")
    self.g.add_node("B")
    self.g.add_node("C")
    self.g.add_node("D")
    self.g.add_node("E")
    self.g.add_distance("A", "B", 5)
    self.g.add_distance("B", "C", 4)
    self.g.add_distance("C", "D", 8)
    self.g.add_distance("D", "C", 8)
    self.g.add_distance("D", "E", 6)
    self.g.add_distance("A", "D", 5)
    self.g.add_distance("C", "E", 2)
    self.g.add_distance("E", "B", 3)
    self.g.add_distance("A", "E", 7)

  def test_node_distance(self):
    self.assertEqual(5, self.g.distance("A", "B"))

  def test_near_to(self):
    self.assertTrue(self.g.near_to("B", "C"))

  def test_add_node(self):
    self.g.add_node("X")
    self.assertIn("X", self.g.nodes)

  def test_add_distance(self):
    self.g.add_distance("B", "A", 10)
    self.assertEqual(10, self.g.distance("B", "A"))


class FunctionsTest(unittest.TestCase):

  def setUp(self):
    self.g = Graph()
    self.g.add_node("A")
    self.g.add_node("B")
    self.g.add_node("C")
    self.g.add_node("D")
    self.g.add_node("E")
    self.g.add_distance("A", "B", 5)
    self.g.add_distance("B", "C", 4)
    self.g.add_distance("C", "D", 8)
    self.g.add_distance("D", "C", 8)
    self.g.add_distance("D", "E", 6)
    self.g.add_distance("A", "D", 5)
    self.g.add_distance("C", "E", 2)
    self.g.add_distance("E", "B", 3)
    self.g.add_distance("A", "E", 7)

  def test_calculate_distance(self):
    self.assertEqual(9, distance(self.g, "A", "B", "C"))

  def test_calculate_wrong_distance(self):
    self.assertEqual('NO SUCH ROUTE', distance(self.g, "A", "E", "D"))

  def test_shortest_distance(self):
    self.assertEqual( 9, dist_to(self.g, "A", "C"))

if __name__ == '__main__':
    unittest.main()