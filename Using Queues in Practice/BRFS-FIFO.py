# This file follows a search algorithm as same as queue implementation that satisfies a particular condition by exploring the graph in concentric layers or levels.

# Using source node can arbitrarily choose a source node and a destination node. This algorithm is not reliable but unless the graph is in tree data structure, in which it typically starts at the root node.

# Importing this library helps the methods, functions, and arguments on specified algorithm which can help cross-check for future implementation.
import networkx as nx
from graph import City, load_graph

# This def function argument are returning a value whose boolean operators are considered between the 20th century.
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)
print("")
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("\n✅ Found:", node.name, node.year, "\n")
        break   
else:
    print("\n📎None Found\n")