# Importing the module to display the stored data on the dictionary attribute extracted from the roadmap.dot file through graph.py syntax, classification, and formatting.
from graph import City, load_graph

# Parameters in the load_graph are inherited from the graph.py file.
nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)
print(f"\n{nodes['bangor']}\n")