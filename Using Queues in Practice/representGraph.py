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