def grid_2d(grid_size, node):
    neighbors = [
        (node[0] - 1, node[1]),
        (node[0] + 1, node[1]),
        (node[0], node[1] - 1),
        (node[0], node[1] + 1)
    ]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < grid_size and 0 <= n[1] < grid_size]
    return [(n, 1) for n in valid_neighbors]

def weighted_graph(graph, node):
    return graph.get(node, [])