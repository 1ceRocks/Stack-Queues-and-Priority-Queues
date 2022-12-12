# Priority Queues Python File
# In this file, we need to create a different hierarchy for each process as the concept program subsides with priority queues. There is also an insertion order for us to determine on which new element is labeled for dequeueing. It's like removing the element from the highest priority as first iteration up to the least priority itself.

# For best manipulation efficiency, we will use the heap data structure algorithm.
from heapq import heappush # heapq module is used for O(log(n)) data volumes.

fruits = [] # Fruits variable empty list.