# Queues Python File
# In this file we will import the Queues module and create the bare-bones queue object needed for enqueue and dequeue operations.

# Importing the Queues module from Python
from collections import deque
# Importing a local module for testing out our FIFO queue.
from queues import Queue

# Class variables for the queue implementation of enqueue and dequeue.
class Queue:
    def __init__(self):
        self.elements = deque()
    
    # Enqueue a single element to the queue and return the element itself to the caller as a string.
    def enqueue(self, value):
        self.elements.append(value)

    # Dequeue an element from the queue and return it as a string.
    def dequeue(self):
        return self.elements.popleft()

fifo = Queue()
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')