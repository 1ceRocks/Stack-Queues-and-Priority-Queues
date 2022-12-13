# Defining a custom data type for visualizing the thought of graphs in cities and road maps conveniently.

# From this program, we'll need a module and a class package, known as typing.
from typing import NamedTuple

# Configured data class for later cases such as the requirement of networkx.
# This is also comparable that is hashable out of the box which is essential to visualize the traversal order of the graph.
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float