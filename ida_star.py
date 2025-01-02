from graph import graph
import graph_bounds as graph_bounds
from heuristics import heuristics

ida_star_result = {"path": [], "cost": 0.0}
# Initialize the start node and the goal node
start = graph_bounds.start
goal = graph_bounds.goal


h_costs = heuristics

g_costs = {start: 0}  # g-cost for the start node is 0
parent = {start: None} 

# Open list (nodes to be evaluated)
open_list = [start]
f_costs = {} # do nothing here, using inside loop


def calculate_g_cost(previous_node, edge_distance):
    # Calculate g(n) = g(n-1) + distance
    return g_costs[previous_node] + edge_distance


def reconstruct_path():
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]
    path.reverse() # to Reorder    
    return path