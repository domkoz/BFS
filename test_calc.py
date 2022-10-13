import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_two_vertices_with_simple_path(self):
        graph = {
            '0': ['1'],
            '1': [],
        }
        self.assertEqual(main.bfs(graph, '0'), ['0', '1'])


    def test_cycle(self):
        graph = {
            '0': ['4', '1'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '0'],
        }
        self.assertEqual(main.bfs(graph, '0'), ['0', '1', '2', '3', '4'])




if __name__ == '__main__':
    unittest.main()
