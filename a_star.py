import heapq

def a_star_search(graph, start, goal, get_neighbors, heuristic):
    g = {start: 0}  # Cost from start to current node
    h = {start: heuristic(start, goal)}  # Estimated cost to goal
    f = {start: g[start] + h[start]}  # Total estimated cost through node
    
    # Priority queue of nodes to explore, starting with (f[start], start)
    open_list = [(f[start], start)]
    closed_list = set()  # Nodes already evaluated
    came_from = {}  # For reconstructing the path

    while open_list:
        # Get the node with the lowest f-score
        current_f, current_node = heapq.heappop(open_list)
        
        # Skip if already evaluated (with consistent heuristic, this ensures optimality)
        if current_node in closed_list:
            continue
        
        # Goal found, reconstruct and return the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path
        
        # Mark node as evaluated
        closed_list.add(current_node)
        
        # Explore neighbors
        for neighbor, cost in get_neighbors(graph, current_node):
            tentative_g = g[current_node] + cost  # Cost to reach neighbor
            
            # If this path is better, update it
            if neighbor not in g or tentative_g < g[neighbor]:
                came_from[neighbor] = current_node
                g[neighbor] = tentative_g
                if neighbor not in h:
                    h[neighbor] = heuristic(neighbor, goal)
                f[neighbor] = g[neighbor] + h[neighbor]
                
                # Add to open_list if not already evaluated
                if neighbor not in closed_list:
                    heapq.heappush(open_list, (f[neighbor], neighbor))
    
    return None  # No path found