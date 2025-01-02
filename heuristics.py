import math
from graph import graph
import graph_bounds as graph_bounds
def euclidean_distance(point, goal):
    return math.sqrt((goal[0] - point[0])**2 + (goal[1] - point[1])**2)

heuristics = {}

for node in graph.keys():
    heuristics[node] = euclidean_distance(node, graph_bounds.goal)

# print(str(heuristics).replace(", (","\n(").replace("{","").replace("}",""))