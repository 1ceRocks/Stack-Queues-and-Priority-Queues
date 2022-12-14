# Defining a custom data type for visualizing the thought of graphs in cities and road maps conveniently.

# From this program, we'll need a module and a class package, known as typing.
# Imported networkx to visualize our graph.
from typing import NamedTuple; import networkx as nx
from REFqueues import Queue, Stack # <-- replacing the queue with a stack, it will initially won't mark the source node as visited.

# To recreate the shortest path between the source and destination, we can iteratively look up the dictionary built earlier when we traversed the graph with the breadth-first approach.
# Using Python deque collection with a fast append operation on the left can be helpful. At each iteration, we add the current node to the path and move to the previous node. It repeats these steps until we reach the source node or theres' no previous node.
from collections import deque

# Implementing the first part of Dijkstra's algorithm using the special class MutableMinHeap to enqueue the unvisited nodes.
from math import inf as infinity
from REFqueues import MutableMinHeap, Queue, Stack

# Configured data class for later cases such as the requirement of networkx.
# This is also comparable that is hashable out of the box which is essential to visualize the traversal order of the graph.
class City(NamedTuple): # This class formats the syntax for getting the values from the dictionary.
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    # Defined properly to ensure that these nodes are hashable.
    @classmethod
    # The purpose of from_dict() class is to take a set of dictionary attributes extracted from the DOT relative path file and returns as a new instance of this City class.
    def from_dict(cls, attributes): # This define function classifies the cache from importing the roadmap.dot file
        return cls(
            # The key value pairs of the parameter attribute are with reference on the roadmap.dot file
            name = attributes["xlabel"],
            country = attributes["country"],
            year = int(attributes["year"]) or None,
            latitude = float(attributes["latitude"]),
            longitude = float(attributes["longitude"]),
        )

# This def() function imports the file; more likely a call identifier for preparation to classify its formats and syntax.
# Node_factory takes a set of callable factory by reading the data extracted and builds a mapping of node identifiers to the Object-Oriented representation of the graph nodes.
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data = True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data = True)
    )

# Note that it uses a reference FIFO queue (REFqueues.py) from the queues module to keep track of the node neighbors, ensuring that you’ll explore them in sequence on each layer. The function also marks visited nodes by adding them to a Python set, so that each neighbor is visited at most once.
def breadth_first_traverse(graph, source):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

def breadth_first_search(graph, source, predicate):
    for node in breadth_first_traverse(graph, source):
        if predicate(node):
            return node

# The existing path between the source and destination from this function returns a list of nodes built with another helper function instead of yielding the individual nodes like breadth_first_traverse().
def retrace(previous, source, destination):
    path = deque()

    current = destination
    while current != source:
        path.appendleft(current)
        current = previous.get(current)
        if current is None:
            return None;
    
    path.appendleft(current)
    return list(path)

# After starting at the source node and traversing the entire subgraph of connected nodes, such as Northern Ireland, the dictionary of previous nodes won’t include the destination node. Therefore, retracing will stop immediately and return None, letting it know there’s no path between source and destination.
def connected(graph, source, destination):
    return shortest_path(graph, source, destination) is not None

# This def function will adapt and copy the exiting function of breadth_first_traverse() as this will call the node by reverse tracing (meaning from destination to the source by following its previous nodes).
def shortest_path(graph, source, destination, order_by = None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    while queue:
        node = queue.dequeue()
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor] = node
                if neighbor == destination:
                    return retrace(previous, source, destination)

# This function builds on top of the first one by looping over the yielded nodes, and stops once the current node meets the expected criteria. If none of the nodes make the predicate truthy, then the function implicitly returns None.
def breadth_first_traverse(graph, source):
    queue = Queue(source)
    visited = {source}
    for node in queue:
        yield node
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

# This def() function builds on top of the first one by looping over the yielded nodes, and stops once the current node meets the expected criteria. If none of the nodes make the predicate truthy, then the function implicitly returns None.
# When iterating the neighbors, it reverse their order to account for the LIFO queue's reversal. It won't mark the neighbors as visited immediately after pushing them onto the stack.
def depth_first_traverse(graph, source, order_by = None):
    stack = Stack(source)
    visited = set()
    while stack:
        if (node := stack.dequeue()) not in visited:
            yield node
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            if order_by:
                neighbors.sort(key = order_by)
            for neighbor in reversed(neighbors):
                stack.enqueue(neighbor)

# The depth-first traversal relies on the stack data structure, it can take advantage of the built-in call stack to save the current search path for later backtracking and rewrite the function recursively. The advantage of this approach is that the recursive call stack will not reverse the neighbors when iterating over them, and do not push already visited neighbors onto the stack.
def recursive_depth_first_traverse(graph, source, order_by = None):
    visited = set()

    def visit(node):
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key = order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                yield from visit(neighbor)
    
    return visit(source)

# To be executed from call search() method with the corresponding traversal strategy. It will be tested out on the DFS-LIFO.py
def breadth_first_search(graph, source, predicate, order_by = None):
    return search(breadth_first_traverse, graph, source, predicate, order_by)

def depth_first_search(graph, source, predicate, order_by = None):
    return search(depth_first_traverse, graph, source, predicate, order_by)

def search(traverse, graph, source, predicate, order_by = None):
    for node in traverse(graph, source):
        if predicate(node):
            return node

# Dijkstra’s Algorithm Using a Priority Queue
# Initially, the distance to all destination cities is unknown, so we assign an infinite cost to each unvisited city except for the source, which has a distance equal to zero. Later, when we find a cheaper path to a neighbor, we update its total distance from the source in the priority queue, which rebalances itself so that an unvisited node with the shortest distance will pop up first next time.
def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous = {}
    visited = set()

    unvisited = MutableMinHeap()
    for node in graph.nodes:
        unvisited[node] = infinity
    unvisited[source] = 0

    while unvisited:
        visited.add(node := unvisited.dequeue())
        for neighbor, weights in graph[node].items():
            if neighbor not in visited:
                weight = weight_factory(weights)
                new_distance = unvisited[node] + weight
                if new_distance < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance
                    previous[neighbor] = node

    return retrace(previous, source, destination)