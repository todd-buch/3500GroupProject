import unittest
from a_star import a_star_search
from get_neighbors import grid_2d, weighted_graph
from heuristic_functions import manhattan_distance, zero_heuristic, euclidean_distance, chebyshev_distance

class TestAStarSearch(unittest.TestCase):

    def test_grid_4x4(self):
        # For a 4x4 grid, we use grid_2d as our neighbor function.
        grid_size = 4  # Our "graph" is simply the grid size.
        start = (0, 0)
        goal = (3, 3)
        # Use Manhattan distance as the heuristic for grid-based movement.
        path = a_star_search(grid_size, start, goal, grid_2d, manhattan_distance)
        
        # Verify a valid path is returned
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)
        
        expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
        self.assertEqual(len(path), expected_length)

    def test_weighted_graph(self):
        # Define a simple weighted graph.
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 5)],
            'C': [('D', 1)],
            'D': []
        }
        start = 'A'
        goal = 'D'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        
        # The optimal path for this graph is A -> B -> C -> D.
        expected_path = ['A', 'B', 'C', 'D']
        self.assertEqual(path, expected_path)

    def test_multiple_correct_path(self):
        # Define a more complex weighted graph with additional nodes.
        graph = {
            'A': [('B', 2), ('C', 5)],
            'B': [('C', 1), ('D', 3)],
            'C': [('D', 2), ('E', 3)],
            'D': [('E', 1), ('F', 5)],
            'E': [('F', 2)],
            'F': [('G', 1)],
            'G': []  # Goal node.
        }
        start = 'A'
        goal = 'G'
        # Use the weighted_graph neighbor function with a zero heuristic.
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        
        valid_paths = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['A', 'B', 'C', 'E', 'F', 'G']
        ]
        
        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)
        self.assertIn(path, valid_paths)

    def test_no_path_available(self):
        # Define a weighted graph where the goal is unreachable.
        graph = {
            'A': [('B', 1)],
            'B': [('C', 1)],
            'C': [],    # 'C' has no neighbors, so 'D' will be unreachable.
            'D': []     # Goal node.
        }
        start = 'A'
        goal = 'D'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNone(path)

    def test_start_equals_goal(self):
        # In any graph, if the start equals the goal, the returned path should just contain that single node.
        graph = {
            'A': [('B', 1)],
            'B': [('C', 1)],
            'C': []
        }
        start = 'A'
        goal = 'A'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertEqual(path, [start])

    def test_invalid_start(self):
        '''Test A* when start node does not exist'''
        # Create a graph that does not include the start node 'A'
        graph = {
            'B': [('C', 1)],
            'C': [('D', 1)],
            'D': []
        }
        start = 'A'  # 'A' is not in the graph
        goal = 'D'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNone(path)

    def test_invalid_goal(self):
        '''Test A* when goal node does not exist'''
        # Create a graph where the goal node 'D' is not present
        graph = {
            'A': [('B', 1)],
            'B': [('C', 1)],
            'C': []
        }
        start = 'A'
        goal = 'D'  # 'D' is not in the graph
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNone(path)
 
    def test_trivial_case(self):
        '''Test A* when graph is empty'''
        graph = {}
        start = 'A'
        goal = 'B'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNone(path)

    def test_single_node_graph(self):
        '''Test A* on a graph consisting on a singular node'''
        graph = {
            'A': []
        }
        start = 'A'
        goal = 'A'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertEqual(path, [start])
    
    def test_disconnected_graph(self):
        '''Test A* on a disconnected graph'''
        graph = {
            'A': [('B', 1)],
            'B': [],
            'C': [('D', 1)],
            'D': []
        }
        start = 'A'
        goal = 'C'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNone(path)

    def test_cyclic_graph(self):
        '''Test A* on a clyclic graph'''
        graph = {
            'A': [('B', 1)],
            'B': [('C', 1), ('A', 1)],  # Cycle back to A
            'C': [('D', 1)],
            'D': []
        }
        start = 'A'
        goal = 'D'
        path = a_star_search(graph, start, goal, weighted_graph, zero_heuristic)
        self.assertIsNotNone(path)
    
    # TODO: add tests for the other heuristics

if __name__ == '__main__':
    unittest.main()
