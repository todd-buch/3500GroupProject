import unittest
from a_star import a_star_search, get_neighbors

# (0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
# (1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
# (2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
# (3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
# (4, 0) (4, 1) (4, 2) (4, 3) (4, 4)

# start = (0, 0)
# goal = (4, 4)
# path = a_star_search(start, goal, get_neighbors)
# print("Path:", path)
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