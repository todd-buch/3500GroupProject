import math

def zero_heuristic(node, goal):
    '''Return 0 for all nodes, effectively turning A* into Dijkstra's algorithm.'''
    return 0

def manhattan_distance_2d(node, goal):
    '''Return the Manhattan distance between the current node and the goal node on 2d grid.'''
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def euclidean_distance_2d(node, goal):
    '''Return the Euclidean distance between the current node and the goal node on 2d grid.'''
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)

def chebyshev_distance_2d(node, goal):
    '''Return the Chebyshev distance between the current node and the goal node on 2d grid.'''
    return max( abs(node[0] - goal[0]), abs(node[1] - goal[1]) )

def manhattan_distance_3d(node, goal):
    '''Return the Manhattan distance between the current node and the goal node on 3d grid.'''
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1]) + abs(node[2] - goal[2])

def euclidean_distance_3d(node, goal):
    '''Return the Euclidean distance between the current node and the goal node on 3d grid.'''
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2 + (node[2] - goal[2])**2)

def chebyshev_distance_3d(node, goal):
    '''Return the Chebyshev distance between the current node and the goal node on 3d grid.'''
    return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]), abs(node[2] - goal[2]))
