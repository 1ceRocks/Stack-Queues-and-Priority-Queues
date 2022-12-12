# Queues Python File
# In this file we will import the Queues module and create the bare-bones queue object needed for enqueue and dequeue operations.

# Importing the Queues module
from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()
    
    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        return self.elements.popleft()  