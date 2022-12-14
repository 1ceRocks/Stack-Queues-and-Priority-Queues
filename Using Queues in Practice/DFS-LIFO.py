# Depth-First Search Using LIFO Queue
# In this file we will use an algorithm called Depth First Search traversal method that follows a path from the source node by plunging into the graph as deeply as possible before backtracking to the last edge crossing and trying another branch.

# This time, we will modify the method of networkx: nx.bfs_tree() with nx.dfs_tree()
import networkx as nx
from graph import City, load_graph

# This def function argument are returning a value whose boolean operators are considered between the 20th century.
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

# Facilitating backtracking by replacing the implementation of FIFO queue with a LIFO queue but it will not behave correctly when traversing data tree structures. Organizing graphs and cycles have distinctive qualities, so there's a subtle requirement of additional change in the code. Hence, an unexpected implementation will be created, a stack-based graph traversal, which works on the other side of the page.
nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)
print("")
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("\n✅ Found:", node.name, node.year, "\n")
        break   
else:
    print("\n📎None Found\n")