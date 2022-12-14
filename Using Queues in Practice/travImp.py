# To test out the breadth-first search and traversal implementations in action.
# Replacing the convenience function built into networkx

# Importing networkx library to observe and estimate the shortest distance between cities and roads by identifying their node amount if weight isn't specified in the configuration.
import networkx as nx

from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)

print("\n", city.name, "\n")

# The traversal order is identical on the first attempt with networkx, confirming that the algorithm works correctly for this data set.
for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)
print("")

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

# Shortest Path Using Breadth-First Traversal Order
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path), "")
print("")

# The terminal output doesn't allow the neighbors to be sorted in a particular order.

# Breadth-First Traversal Order helps us determine which path is shortest by keeping a track of the previous node and storing this information as a key-value pair in the dictionary.