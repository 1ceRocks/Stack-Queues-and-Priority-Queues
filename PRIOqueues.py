# Priority Queues Python File
# In this file, we need to create a different hierarchy for each process as the concept program subsides with priority queues. There is also an insertion order for us to determine on which new element is labeled for dequeueing. It's like removing the element from the highest priority as first iteration up to the least priority itself.

# Importing the required Python module and packages for the Priority Queues program rundown.
from collections import deque; from heapq import heappop, heappush
from itertools import count # Implementing the itertools module to count from zero to infinity in a concise way.

# Class variables required to return the values from the Python module.
# The new concept of this program is to show the count() function as an incremental stage that sets its retaining value for every appended element. When tuple is pushed onto the heap, the same latter priority will be the next to dequeued as the earlier element will take the precedence.

# Mixin Class (meaning they are dependent on another class defined in the Python module)
class IterableMixin:
    # Length of the iterable list that by value priority queue.
    def __len__(self):
        return len(self._elements)

    # Iterable constructor 
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# Class Inheritance from the FIFOqueues.py file (appended as a mixin class)
class Queue(IterableMixin):
    def __init__(self, * elements):
        self._elements = deque(elements) # Appending the leading underscore __ on the "element" to provide an internal bit of implementation, which only the class should access and modify.
    
    # Compatible with the len() function/s.
    def __len__(self): # Returns the number of elements in the queue (default is 1).
        return len(self._elements)
    
    # Class instance methods usable such as for loop.
    def __iter__(self): # Returns an iterator of the elements in the queue that are currently enqueued.
        while len(self) > 0:
            yield self.dequeue() # Enqueue the next element in the queue without waiting for the next call to enqueue to complete.
            
    # Enqueue a single element to the queue and return the element itself to the caller as a string.
    def enqueue(self, element):
        self._elements.append(element)

    # Dequeue an element from the queue and return it as a string.
    def dequeue(self):
        return self._elements.popleft()

class PriorityQueue(IterableMixin):
    # Init function for the Priority Queues program itself and its dependencies.
    def __init__(self):
        self._elements = []
        self._counter = count()

    # Inserting an element into the Priority Queue.
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) # Popped value index will cause the ought returning value located to increase by a single digit. So using the negative sign would indicate the last component of the tuple, regardless of its length.
        heappush(self._elements, element)

    # Heappop for dequeueing elements from the Priority Queue.
    def dequeue(self):
        return heappop(self._elements)[-1] # The index of the element to be printed out.

# This variable with values determine the priority stack necessary for comparing them side by side.
URGENT = 3
MEDIOCRE = 2
UNDER_NORMAL_CONDITIONS = 1

# Implemented a descriptive string defining the type of priority queue used in real-time situations.
notification = PriorityQueue()
notification.enqueue_with_priority(MEDIOCRE, 'Acute Rheumatic Fever')
notification.enqueue_with_priority(UNDER_NORMAL_CONDITIONS, 'Bruises and Minor Injuries')
notification.enqueue_with_priority(URGENT, 'Myocardial Infarction')
notification.enqueue_with_priority(MEDIOCRE, 'Asthma Attack')

def emergencyMeasures():
    # Tuple corresponding with the lowest priority in the notification queue.
    print(f"\nPriority Queue")
    print(f"1 - {notification.dequeue()}")
    print(f"2 - {notification.dequeue()}")
    print(f"3 - {notification.dequeue()}")
    print(f"4 - {notification.dequeue()}\n")

emergencyMeasures()