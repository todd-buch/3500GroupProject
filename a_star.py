import heapq

def a_star_search(start, goal, get_neighbors):
   open_list = [(0, start)]  # list of nodes to check out next
   closed_list = set() # set of nodes we've already checked
   g = {start: 0} # how many steps it takes to get to a node from the start
   h = {start: abs(start[0] - goal[0]) + abs(start[1] - goal[1])} # uses Manhattan distance as heuristic
   f = {start: g[start] + h[start]} # estimated total cost from start to goal through node
   came_from = {} # parent node of each node

   while open_list:
      current_f, current_node = heapq.heappop(open_list)
      if current_node in closed_list:
         continue

      if current_node == goal:
         # Reconstruct the path and return
         path = []
         while current_node in came_from:
            path.append(current_node)
            current_node = came_from[current_node]
         path.append(start)
         path.reverse()
         return path

      closed_list.add(current_node) 

      for neighbor in get_neighbors(current_node):
         tentative_g = g[current_node] + 1  # Assuming uniform cost for simplicity
         if neighbor not in g or tentative_g < g[neighbor]:
            came_from[neighbor] = current_node
            g[neighbor] = tentative_g
            h[neighbor] = abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
            f[neighbor] = g[neighbor] + h[neighbor]
            if neighbor not in closed_list:
               heapq.heappush(open_list, (f[neighbor], neighbor))

   return None  # No path found

def get_neighbors(node):
   neighbors = [
      (node[0] - 1, node[1]),
      (node[0] + 1, node[1]),
      (node[0], node[1] - 1),
      (node[0], node[1] + 1)
   ]
   # Filter out neighbors that are out of bounds or obstacles
   return [n for n in neighbors if 0 <= n[0] < 5 and 0 <= n[1] < 5]