# Defining a custom data type for visualizing the thought of graphs in cities and road maps conveniently.

# From this program, we'll need a module and a class package, known as typing.
# Imported networkx to visualize our graph.
from typing import NamedTuple; import networkx as nx
from REFqueues import Queue

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

def breadth_first_search(graph, source, predicate):
    for node in breadth_first_traverse(graph, source):
        if predicate(node):
            return node

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