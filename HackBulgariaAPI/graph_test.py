import unittest
from graph import DirectedGraph

class TestGraph(unittest.TestCase):
	def setUp(self):
		self.test_graph = DirectedGraph()
	def test_init(self):
		self.assertEqual(self.test_graph.graph, {})
	def test_add_edge(self):
		self.test_graph.addEdge("a", "b")
		self.test_graph.addEdge("a", "c")
		self.assertIn("a", self.test_graph.graph)
		self.assertIn("b", self.test_graph.graph["a"])
		self.assertIn("c", self.test_graph.graph["a"])
	def test




if __name__ == '__main__':
	unittest.main()