# Importing the module to display the stored data on the dictionary attribute extracted from the roadmap.dot file through graph.py syntax, classification, and formatting.
from graph import City, load_graph, shortest_path, connected

# Importing networkx library to observe and estimate the shortest distance between cities and roads by identifying their node amount if weight isn't specified in the configuration.
import networkx as nx

# Parameters in the load_graph are inherited from the graph.py file.
nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Road Map of the United Kingdom/roadmap.dot", City.from_dict)
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

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

# Shortest Path Using Breadth-First Traversal Order
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path), "")
print("")

# This first path follows the natural order of neighbors from the DOT file.
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)), "\n")

# To govern a descending order, we add the minus sign (-) in front of the .latitude attribute.
def by_latitude(city):
    return -city.latitude

# This second path prefers neighbors with a higher latitude, which we specify through a custom sort strategy.
print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)), "\n")

# Verifying the retrace() function by letting it know that there's no path between source and destination.
print(connected(graph, nodes["belfast"], nodes["glasgow"]))
print(connected(graph, nodes["belfast"], nodes["derry"]), "\n")