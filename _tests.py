open_list = [start]
closed_set = set()

# Initial f_limit based on the start node
f_limit = h_costs[start] + g_costs[start]  # Only h_costs[start] is typically used if g_cost is 0 initially

def calculate_g_cost(previous_node, edge_distance):
    # Calculate g(n) = g(n-1) + distance
    return g_costs[previous_node] + edge_distance

def reconstruct_path():
    path = []
    def reconstructor(current_node):
        if current_node is None:
            return path
        path.append(current_node)
        return reconstructor(parent[current_node])

    path = reconstructor(goal)
    path.reverse()  # Reverse the path to start from the beginning
    return path

# Expansion tracker
expansion = []

while True:
    tentative_current = open_list[0]
    i = 0
    
    # Iteratively deepen based on f_limit
    while f_costs[tentative_current] <= f_limit:
        i += 1
        print("Expanding:", tentative_current)
        tentative_current = open_list[i]  # Advance to the next node
    
    current = tentative_current  # Set the current node after thresholding
    
    # Your remaining code here...
    
    break