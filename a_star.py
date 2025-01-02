from graph import graph
import graph_bounds as graph_bounds
from heuristics import heuristics

a_star_result = {"path": [], "cost": 0.0}
# Initialize the start node and the goal node
start = graph_bounds.start
goal = graph_bounds.goal


h_costs = heuristics

g_costs = {start: 0}  # g-cost for the start node is 0
parent = {start: None}  # parent of each node ,use to reconstruction of the path later

# Open list (nodes to be evaluated)
open_list = [start]
f_costs = {} # do nothing here, using inside loop


def calculate_g_cost(previous_node, edge_distance):
    # Calculate g(n) = g(n-1) + distance
    return g_costs[previous_node] + edge_distance


# def reconstruct_path():
#     path = []
#     current_node = goal
#     while current_node is not None:
#         path.append(current_node)
#         current_node = parent[current_node]
#     path.reverse() # to Reorder    
#     return path

def reconstruct_path():
    path = []
    def reconstructor(current_node):
        if current_node is None:
            return path
        path.append(current_node)
        print(path)
        return reconstructor(parent[current_node])

    path = reconstructor(goal)
    path.reverse() # to Reorder    
    return path

# Main A* algorithm loop
while open_list:
    # print(open_list)

    # Get the node with the lowest g-cost + h-cost (f-cost)
    f_costs = {node: g_costs[node] + h_costs[node] for node in open_list}
    # print(f_costs)    
    current_node = min(f_costs, key = f_costs.get)
    
    # If the current node is the goal, reconstruct the path
    if current_node == goal:
        a_star_result = {"path": reconstruct_path(), "cost": g_costs[goal]}
        print("a_star", a_star_result)
        break
    
    # Removing current selected node from open list 
    open_list.remove(current_node)
    # Iterate through neighbors of the current node
    for neighbor, edge_distance in graph.get(current_node, []): #  [] is for when there is no neighbor(s)
        tentative_g_cost = calculate_g_cost(current_node, edge_distance) 
        
        # If this new g-cost is lower than the previously recorded g-cost for this neighbor
        if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
            g_costs[neighbor] = tentative_g_cost
            parent[neighbor] = current_node  # Update parent
            
            # Add the neighbor to the open list if not already in it
            if neighbor not in open_list:
                open_list.append(neighbor)
