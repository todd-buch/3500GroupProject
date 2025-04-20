import unittest
from a_star import a_star_search
from get_neighbors import grid_2d
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

    # TODO: add tests for the other heuristics

if __name__ == '__main__':
    unittest.main()
