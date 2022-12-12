# Queues Python File
# In this file we will import the Queues module and create the bare-bones queue object needed for enqueue and dequeue operations.

# Importing the Queues module from Python
from collections import deque
# Importing a local module for testing out our FIFO queue.
# from queues import Queue

# Class variables for the queue implementation of enqueue and dequeue.
# Improving our enqueued elements on class by making it iterable and be able to report its length and optionally accept initial elements (see the commit for appended code changes).
class Queue:
    def __init__(self, * elements):
        self.__elements = deque(elements) # Appending the leading underscore __ on the "element" to provide an internal bit of implementation, which only the class should access and modify.
    
    def __len__(self):
        return len(self.__elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            
    # Enqueue a single element to the queue and return the element itself to the caller as a string.
    def enqueue(self, element):
        self.__elements.append(element)

    # Dequeue an element from the queue and return it as a string.
    def dequeue(self):
        return self.__elements.popleft()

# Main functions for testing out our FIFO queue implementation.
fifo = Queue()
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')

print(fifo.dequeue())