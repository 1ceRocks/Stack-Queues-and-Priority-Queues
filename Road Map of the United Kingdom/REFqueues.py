# FIFO (First In First Out) Queues Python File
# In this file we will import the Queues module and create the bare-bones queue object needed for enqueue and dequeue operations.

# Importing the Queues module from Python
# Complete syntax for the mutable min-heap
from collections import deque
from heapq import heappush, heappop, heapify
from itertools import count
from dataclasses import dataclass
from itertools import count
from typing import Any

# Internally, this specialized priority queue stores data class elements instead of tuples because the elements must be mutable. Notice the additional order flag, which makes the elements comparable, just like tuples:

# Refactoring the Code Using a Mixin Class
class IterableMixin:                    
    # Compatible with the len() function/s.
    def __len__(self): # Returns the number of elements in the queue (default is 1).
        return len(self._elements)

    # Class instance methods usable such as for loop.
    def __iter__(self): # Returns an iterator of the elements in the queue that are currently enqueued.
        while len(self) > 0:
            yield self.dequeue() # Enqueue the next element in the queue without waiting for the next call to enqueue to complete.

# Class variables for the queue implementation of enqueue and dequeue.
# Improving our enqueued elements on class by making it iterable and be able to report its length and optionally accept initial elements (see the commit for appended code changes).
class Queue(IterableMixin):
    def __init__(self, * elements):
        self._elements = deque(elements) # Appending the leading underscore __ on the "element" to provide an internal bit of implementation, which only the class should access and modify.
            
    # Enqueue a single element to the queue and return the element itself to the caller as a string.
    def enqueue(self, element):
        self._elements.append(element)

    # Dequeue an element from the queue and return it as a string.
    def dequeue(self):
        return self._elements.popleft()

# Building Stack(LIFO) data type
class Stack(Queue): # <-- Inheritance
    def dequeue(self):
        return self._elements.pop() # pop() gets and removes the last element on the data.

# Building a Priority Queue Data Type
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) # the _counter will be responsible for handling 
                                                            # the same priority description making the 
                                                            # first enqueued be the first by default.  
        heappush(self._elements, element) # rearranging heappush parameters
    def dequeue(self):
        return heappop(self._elements)[-1] # to indicate the last component of the tuple, 
                                            #regardless of its length, -1 was implemented as the index 
                                            # of the tuple

# Mutable version of a min-heap 
@dataclass(order=True) # order flag, which makes the elements comparable(just like tuples)
class Element:
    priority: float
    count: int
    value: Any

# The square bracket syntax behaves mostly the same as a regular priority queue operation like before, but this time it allows us to peek or modify the priority of an element.
class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value

# Main functions for testing out our FIFO queue implementation.
# This would be unnecessary if elements line 41 was already defined into a variable (fifo).
# fifo = Queue()
# fifo.enqueue('First')
# fifo.enqueue('Second')
# fifo.enqueue('Third')

# Class for testing out our FIFO queue implementation
# def main():
#     fifo = Queue('First', 'Second', 'Third') # Create a FIFO queue with two elements each of which should be enqueued together.
#     print(f"\n{len(fifo)} - before iteration (elements are not yet dequeued)") # Len queue is still not called yet so the value here would always be 3.
#     # For loop reduces its size on each single file element to be called once per queue by dequeueing elements from itself as we iterate through them.n
#     for element in fifo: 
#         print(element)
#     print(f"{len(fifo)} - after iteration (elements are dequeued)\n") # Len queue has been iterated so no element is currently queued, the value here would always be 0.
 
# main() # Def caller function for testing out our FIFO queue implementation.