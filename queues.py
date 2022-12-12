# Queues Python File
# In this file we will import the Queues module and create the bare-bones queue object needed for enqueue and dequeue operations.

# Importing the Queues module
from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()