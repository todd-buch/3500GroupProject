def grid_2d(grid_size, node):
    neighbors = [
        (node[0] - 1, node[1]),
        (node[0] + 1, node[1]),
        (node[0], node[1] - 1),
        (node[0], node[1] + 1)
    ]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < grid_size and 0 <= n[1] < grid_size]
    return [(n, 1) for n in valid_neighbors]

def grid_3d(grid_size, node):
    neighbors = [
        (node[0] - 1, node[1], node[2]),
        (node[0] + 1, node[1], node[2]),
        (node[0], node[1] - 1, node[2]),
        (node[0], node[1] + 1, node[2]),
        (node[0], node[1], node[2] - 1),
        (node[0], node[1], node[2] + 1)
    ]
    valid_neighbors = [n for n in neighbors if all(0 <= coord < grid_size for coord in n)]
    return [(n, 1) for n in valid_neighbors]
