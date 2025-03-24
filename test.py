from a_star import a_star_search, get_neighbors

# (0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
# (1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
# (2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
# (3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
# (4, 0) (4, 1) (4, 2) (4, 3) (4, 4)

start = (0, 0)
goal = (4, 4)
path = a_star_search(start, goal, get_neighbors)
print("Path:", path)