# Importing the module to display the stored data on the dictionary attribute extracted from the roadmap.dot file through graph.py syntax, classification, and formatting.
from graph import City, load_graph

# Parameters in the load_graph are inherited from the graph.py file.
nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)
print(f"\n{nodes['bristol']}")
print(f"{graph}\n")

# The method neighbors() identifies the neighboring cities immediately with nodes[] as the argument within the given subgraph information on the DOT file. Available routes, estimated travel times, distances, possible weights, and connecting edges to follow are still yet to be considered.
for neighbor in graph.neighbors(nodes["bristol"]):
    print(neighbor.name)
print("")

# In this program output, the map specifications are portrayed in digits to represent their distance.
for neighbor, weights in graph[nodes["bristol"]].items():
    print(weights["distance"], neighbor.name)
print("")

# Defined a helper function that returns a list of neighbors and their weights sorted by the specified strategy.

# It takes a dictionary of all the weights associated with an edge argument and finally returns a sorting key.
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key = lambda item: strategy(item[1]))

# Defined a concrete strategy that produces a floating-point distance based on the input dictionary.
def by_distance(weights):
    return float(weights["distance"])

# This will iterate over the neighbors of Bristol, sorted by distance in ascending order.
for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
print("")