# This file follows a search algorithm as same as queue implementation that satisfies a particular condition by exploring the graph in concentric layers or levels.

# Using source node can arbitrarily choose a source node and a destination node. This algorithm is not reliable but unless the graph is in tree data structure, in which it typically starts at the root node.

# Importing this library helps the methods, functions, and arguments on specified algorithm which can help cross-check for future implementation.
import networkx as nx
from graph import City, load_graph

# This def function argument are returning a value whose boolean operators are considered between the 20th century.
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

# Source node. This function is in sequential order without interruption before moving to the next layer of the graph. The subsequent layer consists of the second-level neighbors starting from the source node.
nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Road Map of the United Kingdom/roadmap.dot", City.from_dict)
print("")
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("๐", node.name)
    if is_twentieth_century(node.year):
        print("\nโ Found:", node.name, node.year, "\n")
        break   
else:
    print("\n๐None Found\n")

# Determining the latitude of city by iterating them in sorted order. reverse = True means the exact opposite direction of the graph in concentric layers or levels.
def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key = by_latitude, reverse = True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("๐", node.name)
    if is_twentieth_century(node.year):
        print("\nโ Found:", node.name, node.year, "\n")
        break
else:
    print("\n๐None Found\n")

# The terminal output should be different since higher and lower latitude is compared like the Newcastle since it does have a greater amount of latitude compared to Carlisle and therefore is visited.