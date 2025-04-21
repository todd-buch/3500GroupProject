import unittest
from random import randint
from a_star import a_star_search
from get_neighbors import grid_2d
from get_neighbors import grid_3d
from heuristic_functions import manhattan_distance, zero_heuristic, euclidean_distance, chebyshev_distance
from heuristic_functions import manhattan_distance_3d, euclidean_distance_3d, chebyshev_distance_3d

heuristics_2d = {
    "Manhattan": manhattan_distance,
    "Euclidean": euclidean_distance,
    "Chebyshev": chebyshev_distance,
    "Zero": zero_heuristic
}
heuristics_3d = {
    "Manhattan": manhattan_distance_3d,
    "Euclidean": euclidean_distance_3d,
    "Chebyshev": chebyshev_distance_3d,
    "Zero": zero_heuristic
}

class TestAStarSearch(unittest.TestCase):
    '''
    Test A* algorithm for correct functionality in the following scenarios:
    - Different dimension input grids (2d and 3d)
    - Different sizes of input grids
    - Various edge cases (No possible path, Start equals goal etc.)
    - Random grids, starts and destinations
    '''


    def test_empty_grid_2d(self):
        '''Testing the trivial case - 0x0 2d grid'''
        grid_size = 0
        start = (0, 0)
        goal = (0, 0)

        # Iterate through each heuristic for 2d grids
        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                # Create graph and test for correct output path
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                # Test for correct output path length
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                self.assertEqual(len(path), expected_length)

    def test_grid_4x4_2d(self):
        '''Testing small 2d grid (4x4)'''
        grid_size = 4
        start = (0, 0)
        goal = (3, 3)

        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                self.assertEqual(len(path), expected_length)

    def test_grid_1000x1000_2d(self):
        '''Testing large 2d grid (1000x1000)'''
        grid_size = 1000
        start = (0, 0)
        goal = (99, 99)

        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                self.assertEqual(len(path), expected_length)

    def test_no_possible_path_2d(self):
        '''Test when no possible path exists between start and path'''
        grid_size = 10
        start = (0, 0)
        goal = (10, 10) # Goal is outside of grid bounds

        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path, [])
                expected_length = 0
                self.assertEqual(len(path), expected_length)

    def test_start_equals_goal_2d(self):
        '''Test when start and goal nodes are the same'''
        grid_size = 10
        start = (7, 7)
        goal = (7, 7) # Goal is the same as the start and within grid bounds

        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                self.assertEqual(len(path), expected_length)

    def test_random_grids_2d(self):
        '''Test various randomized 2d grids and inputs'''
        for _ in range(25):
            grid_size = randint(1, 100)
            start = (randint(0, grid_size-1), randint(0, grid_size-1))
            goal = (randint(0, grid_size-1), randint(0, grid_size-1))

            for name, heuristic in heuristics_2d.items():
                with self.subTest(heuristic=name):
                    path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                    self.assertIsNotNone(path)
                    self.assertEqual(path[0], start)
                    self.assertEqual(path[-1], goal)
                    expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                    self.assertEqual(len(path), expected_length)

    def test_edge_traversal_2d(self):
        '''Test when optimal path is along grid edge'''
        grid_size = 5
        start = (0, 0)
        goal = (0, 4)  # Travel along edge only
        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + 1
                self.assertEqual(len(path), expected_length)


    def test_empty_grid_3d(self):
        '''Test the trivial case'''
        grid_size = 0
        start = (0, 0, 0)
        goal = (0, 0, 0)

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)

    def test_grid_3x3x3_3d(self):
        '''Test small 3d grid'''
        grid_size = 3
        start = (0, 0, 0)
        goal = (2, 2, 2)

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)

    def test_grid_1000x1000x1000_3d(self):
        '''Test large 3d grid'''
        grid_size = 1000
        start = (0, 0, 0)
        goal = (49, 49, 29)

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + abs(goal[2] - start[2]) + 1
                self.assertEqual(len(path), expected_length)

    def test_no_possible_path_3d(self):
        '''Test 3d graph without any possible path between start and goal'''
        grid_size = 10
        start = (0, 0, 0)
        goal = (10, 10, 10)  # Goal outside grid bounds

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path, [])
                self.assertEqual(len(path), 0)

    def test_start_equals_goal_3d(self):
        '''Test when start coordinate is same as goal coordinate'''
        grid_size = 10
        start = (5, 5, 5)
        goal = (5, 5, 5)

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                self.assertEqual(len(path), 1)

    def test_random_grids_3d(self):
        '''Test randomized 3d grids'''
        for _ in range(25):
            grid_size = randint(1, 50)
            start = (randint(0, grid_size - 1), randint(0, grid_size - 1), randint(0, grid_size - 1))
            goal = (randint(0, grid_size - 1), randint(0, grid_size - 1), randint(0, grid_size - 1))

            for name, heuristic in heuristics_3d.items():
                with self.subTest(heuristic=name):
                    path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                    self.assertIsNotNone(path)
                    self.assertEqual(path[0], start)
                    self.assertEqual(path[-1], goal)
                    expected_length = abs(goal[0] - start[0]) + abs(goal[1] - start[1]) + abs(goal[2] - start[2]) + 1
                    self.assertEqual(len(path), expected_length)

    def test_edge_traversal_3d(self):
        '''Test when optimal path travels up the edge'''
        grid_size = 5
        start = (0, 0, 0)
        goal = (0, 0, 4)  # Travel along edge only

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[2] - start[2]) + 1
                self.assertEqual(len(path), expected_length)

    def test_corner_to_corner_3d(self):
        '''Test the furthest possible distance between start and goal'''
        grid_size = 10
        start = (0, 0, 0)
        goal = (9, 9, 9)  # From one corner to the opposite corner

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = sum(abs(goal[i] - start[i]) for i in range(3)) + 1
                self.assertEqual(len(path), expected_length)

    def test_single_layer_grid_3d(self):
        '''Test 3d grid when start and goal are on same level'''
        grid_size = 1
        start = (0, 0, 0)
        goal = (0, 0, 0)  # Only one possible node

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertEqual(path, [start])
                self.assertEqual(len(path), 1)

    def test_large_sparse_grid_3d(self):
        '''Test large grid'''
        grid_size = 100
        start = (0, 0, 0)
        goal = (0, 0, 59)  # Straight line traversal along one dimension

        for name, heuristic in heuristics_3d.items():
            with self.subTest(heuristic=name):
                path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path[0], start)
                self.assertEqual(path[-1], goal)
                expected_length = abs(goal[2] - start[2]) + 1
                self.assertEqual(len(path), expected_length)

    def test_random_start_goal_at_boundaries_3d(self):
        '''Test randomized boundaries, start and goal'''
        grid_size = 50
        boundaries = [0, grid_size - 1]

        for _ in range(10):
            start = (randint(0, grid_size - 1), randint(0, grid_size - 1), boundaries[randint(0, 1)])
            goal = (boundaries[randint(0, 1)], randint(0, grid_size - 1), randint(0, grid_size - 1))

            for name, heuristic in heuristics_3d.items():
                with self.subTest(heuristic=name, start=start, goal=goal):
                    path = a_star_search(grid_size, start, goal, grid_3d, heuristic)
                    self.assertIsNotNone(path)
                    self.assertEqual(path[0], start)
                    self.assertEqual(path[-1], goal)
                    expected_length = sum(abs(goal[i] - start[i]) for i in range(3)) + 1
                    self.assertEqual(len(path), expected_length)

if __name__ == '__main__':
    unittest.main()
