def zero_heuristic(node, goal):
    '''Return 0 for all nodes, effectively turning A* into Dijkstra's algorithm.'''
    return 0

def manhattan_distance(node, goal):
    '''Return the Manhattan distance between the current node and the goal node. Only works for 2D grids.'''
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# TODO: add other heuristic functions that prof said to use