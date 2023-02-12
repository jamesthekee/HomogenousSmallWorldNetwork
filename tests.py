import unittest
from hswn import *

# param_list = [(50, 4, 0), (100, 6, 0.5), (200, 8, 0.9), (200, 8, 5)]


class TestGraphProperties(unittest.TestCase):

    def test_degree(self):
        degrees = list(zip(*self.graph.degree))[1]
        self.assertTrue(len(set(degrees)) == 1)

    def test_selfloops(self):
        for node in self.graph.nodes:
            self.assertFalse(self.graph.has_edge(node, node))

    def test_doubleedge(self):
        # If algorithm tried to add double-edge there will be 1 less edge than the expected total.
        # as networkx doesn't allow double-edges
        self.assertTrue(len(self.graph.edges) == self.N*self.K//2)

    def setUp(self) -> None:
        self.N = 50
        self.K = 4
        self.graph = homogeneous_small_word_graph(self.N, self.K, 0.5)


if __name__ == '__main__':
    unittest.main()

