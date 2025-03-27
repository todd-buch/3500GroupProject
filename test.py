import unittest, heuristic_functions, get_neighbors
from a_star import a_star_search

# Example usage:
# When we want a 2D grid, graph is equal to the size of the grid (e.g., 5 = 5x5 grid, 10 = 10x10 grid)
# graph = 5
# graph = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('A', 4), ('D', 3)],
#     'C': [('A', 2), ('D', 5)],
#     'D': [('B', 3), ('C', 5)]
# }

start = (0, 0)
goal = (4, 4)
graph_2d = 5
path1 = a_star_search(graph_2d, start, goal, get_neighbors.grid_2d, heuristic_functions.manhattan_distance)
print("Test1:", path1)

graph2 = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 3)],
    'C': [('A', 2), ('D', 5)],
    'D': [('B', 3), ('C', 5)]
}
start = 'A'
goal = 'D'
path2 = a_star_search(graph2, start, goal, get_neighbors.weighted_graph, heuristic_functions.zero_heuristic)
print("Test2:", path2)

class Test_a_star(unittest.TestCase):
    def test_invalid_start(self):
        '''Test A* when start node does not exist'''
        pass

    def test_invalid_goal(self):
        '''Test A* when goal node does not exist'''
        pass
 
    def test_trivial_case(self):
        '''Test A* when graph is empty'''
        pass

    def test_single_node_graph(self):
        '''Test A* on a graph consisting on a singular node'''
        pass
    
    def test_start_same_as_end(self):
        '''Test A* when start node is same as goal node'''
        pass

    def test_small_graph(self):
        '''Test A* on a small graph'''
        pass
    
    def test_no_solution_graph(self):
        '''Test A* on a graph that does not have a path from start node to goal node'''
        pass

    def test_multiple_correct_path(self):
        '''Test A* on a graph that includes multiple corrects paths from start node to goal nodes'''
        pass

    def test_disconnected_graph(self):
        '''Test A* on a disconnected graph'''
        pass

    def test_cyclic_graph(self):
        '''Test A* on a clyclic graph'''
        pass

if __name__ == '__main__':
    unittest.main()