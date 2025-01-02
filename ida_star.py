from graph import graph
import graph_bounds as graph_bounds
from heuristics import heuristics as h_costs

def ida_star(graph, start, goal, h_costs):
    # Helper function to perform depth-first search with a given cost limit
    def dfs(node, g_cost, limit, path, visited):
        f_cost = g_cost + h_costs[node]
        
        # If the f-cost exceeds the limit, return the f-cost for pruning
        if f_cost > limit:
            return f_cost
        
        # If the goal is found, return the path
        if node == goal:
            return path
        
        visited.add(node)  # Mark the node as visited

        # Explore neighbors
        min_cost = float('inf')
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_g_cost = g_cost + edge_cost
                result = dfs(neighbor, new_g_cost, limit, new_path, visited)

                # If the goal is found, return the path
                if isinstance(result, list):  # if the result is a path, return it
                    return result
                
                # Otherwise, track the minimum f-cost encountered
                min_cost = min(min_cost, result)

        visited.remove(node)  # Unmark the node

        return min_cost  # Return the minimum f-cost found

    # Initial limit on f-cost (start with the heuristic cost of the start node)
    limit = h_costs[start]
    path = None

    # Repeat the search with increasing limits until a solution is found
    while path is None:
        visited = set()
        result = dfs(start, 0, limit, [start], visited)

        if isinstance(result, list):
            path = result  # If the result is a path, return it
        else:
            limit = result  # If not, increase the limit and try again

    return path
path = ida_star(graph, graph_bounds.start, graph_bounds.goal, h_costs)
print("Path found:", path)