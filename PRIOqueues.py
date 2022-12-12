# Priority Queues Python File
# In this file, we need to create a different hierarchy for each process as the concept program subsides with priority queues. There is also an insertion order for us to determine on which new element is labeled for dequeueing. It's like removing the element from the highest priority as first iteration up to the least priority itself.

# Importing the required Python module and packages for the Priority Queues program rundown.
from collections import deque; from heapq import heappop, heappush

# Class variables required to return the values from the Python module.
class PriorityQueue:
    def __init__(self):
        self.elements = []