# Object Representation of the United Kingdom Python File
# Implementing classical graph using queues by visualizing nodes in a sample country that represents a map between roads and cities. Queues contain the general idea for creating an optimal path between cities but merely accounts nothing on the official road types, schedules, rules, capacity, traffic, and other bypasses on that particular information.

# pygraphviz and networkx libraries are the only libraries that would be useful throughout this program as well as the DOT graph file from the source code material.
import networkx as nx # With the help of pygraphviz (acting as third-party library), it provides functions that delegate this task and manipulate the coordinates of the graph in the sample DOT file.
# print(nx.nx_agraph.read_dot("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot"))

#Testing out one string map from the roadmap file to a corresponding dictionary of keyvalue pairs.
graphTest = nx.nx_agraph.read_dot("Stack-Queues-and-Priority-Queues/Road Map of the United Kingdom/roadmap.dot")
print(f"\n{graphTest}")
print(f"{graphTest.nodes['bristol']}\n")