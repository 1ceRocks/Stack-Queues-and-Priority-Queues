# Priority Queues Python File
# In this file, we need to create a different hierarchy for each process as the concept program subsides with priority queues. There is also an insertion order for us to determine on which new element is labeled for dequeueing. It's like removing the element from the highest priority as first iteration up to the least priority itself.

# Importing the required Python module and packages for the Priority Queues program rundown.
from collections import deque; from heapq import heappop, heappush
from queues import PriorityQueue

# Class variables required to return the values from the Python module.
class PriorityQueue:
    # Init function for the Priority Queues program itself and its dependencies.
    def __init__(self):
        self.elements = []

    # Inserting an element into the Priority Queue.
    def enqueue_with_priority(self, priority, value):
        heappush(self.elements, (priority, value))

    # Heappop for dequeueing elements from the Priority Queue.
    def dequeue(self):
        return heappop(self.elements)

# This variable with values determine the priority stack necessary for comparing them side by side.
URGENT = 3
MEDIOCRE = 2
UNDER_NORMAL_CONDITIONS = 1