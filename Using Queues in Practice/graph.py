# Defining a custom data type for visualizing the thought of graphs in cities and road maps conveniently.

# From this program, we'll need a module and a class package, known as typing.
# Imported networkx to visualize our graph.
from typing import NamedTuple; import networkx as nx

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
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data = True)
    }