# Test-driving the Dijkstra’s algorithm interactively and compare it against the networkx implementation:
import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph("Stack-Queues-and-Priority-Queues/Using Queues in Practice/roadmap.dot", City.from_dict)

city1 = nodes["london"]
city2 = nodes["edinburgh"]

def distance(weights):
    return float(weights["distance"])

print("")
for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)
print("")

def weight(node1, node2, weights):
    return distance(weights)

print("")
for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)
print("")

# Success! Both functions yield exactly the same shortest path between London and Edinburgh.