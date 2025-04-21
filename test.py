import unittest
from random import randint
from a_star import a_star_search
from get_neighbors import grid_2d
from heuristic_functions import manhattan_distance, zero_heuristic, euclidean_distance, chebyshev_distance

heuristics_2d = {
    "Manhattan": manhattan_distance,
    "Euclidean": euclidean_distance,
    "Chebyshev": chebyshev_distance,
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
        # Testing the trivial case - 0x0 2d grid
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
        # Testing small 2d grid (4x4)
        grid_size = 4
        start = (0, 0)
        goal = (3, 3)

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

    def test_grid_1000x1000_2d(self):
        # Testing large 2d grid (1000x1000)
        grid_size = 1000
        start = (0, 0)
        goal = (99, 99)

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

    def test_no_possible_path_2d(self):
        # Test when no possible path exists between start and path
        grid_size = 10
        start = (0, 0)
        goal = (10, 10) # Goal is outside of grid bounds

        # Iterate through each heuristic for 2d grids
        for name, heuristic in heuristics_2d.items():
            with self.subTest(heuristic=name):
                # Create graph and test for correct output path
                path = a_star_search(grid_size, start, goal, grid_2d, heuristic)
                self.assertIsNotNone(path)
                self.assertEqual(path, [])
                # Test for correct output path length
                expected_length = 0
                self.assertEqual(len(path), expected_length)

    def test_start_equals_goal_2d(self):
        # Test when start and goal nodes are the same
        grid_size = 10
        start = (7, 7)
        goal = (7, 7) # Goal is the same as the start and within grid bounds

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

    def test_random_grids_2d(self):
        # Test various randomized 2d grids and inputs
        for _ in range(25):
            grid_size = randint(1, 100)
            start = (randint(0, grid_size-1), randint(0, grid_size-1))
            goal = (randint(0, grid_size-1), randint(0, grid_size-1))

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


if __name__ == '__main__':
    unittest.main()
