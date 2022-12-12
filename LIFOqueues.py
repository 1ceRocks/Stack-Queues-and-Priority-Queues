# LIFO (Last In First Out) Queues Python File
# In Python file we will create a queue by building a stack data type using class inheritance and .dequeue() to remove elements from the top of the stack.

# All methods and functions in this module are defined from the FIFOqueues.py file but only def function would be modified.

# Importing the Queues module from Python
from collections import deque
# Importing a local module for testing out our LIFO queue.
# from queues import Queue

# Class variables for the queue implementation of enqueue and dequeue.
# Improving our enqueued elements on class by making it iterable and be able to report its length and optionally accept initial elements (see the commit for appended code changes).
class Stack(): # Class Inheritance
    def __init__(self, * elements):
        self.__elements = deque(elements) # Appending the leading underscore __ on the "element" to provide an internal bit of implementation, which only the class should access and modify.
    
    # Compatible with the len() function/s.
    def __len__(self): # Returns the number of elements in the queue (default is 1).
        return len(self.__elements)
    
    # Class instance methods usable such as for loop.
    def __iter__(self): # Returns an iterator of the elements in the queue that are currently enqueued.
        while len(self) > 0:
            yield self.dequeue() # Enqueue the next element in the queue without waiting for the next call to enqueue to complete.
            
    # Enqueue a single element to the queue and return the element itself to the caller as a string.
    def enqueue(self, element):
        self.__elements.append(element)

    # Dequeue an element from the queue and return it as a string.
    def dequeue(self):
        return self.__elements.pop() # From popleft() to pop() (to right) specifically for LIFO queues.

# Main functions for testing out our LIFO queue implementation.
lifo = Stack() # Added class inheritance for caller functions towards this variable.
lifo.enqueue('First')
lifo.enqueue('Second')
lifo.enqueue('Third')

# Class for testing out our lifo queue implementation
def main():
    lifo = Stack('First', 'Second', 'Third') # Create a LIFO queue with two elements each of which should be enqueued together.
    print(f"\n{len(lifo)} - before iteration (elements are not yet dequeued)") # Len queue is still not called yet so the value here would always be 3.
    # For loop reduces its size on each single file element to be called once per queue by dequeueing elements from itself as we iterate through them.
    for element in lifo: 
        print(element)
    print(f"{len(lifo)} - after iteration (elements are dequeued)\n") # Len queue has been iterated so no element is currently queued, the value here would always be 0.
    
main() # Def caller function for testing out our lifo queue implementation.

# Python List - Rudimentary Stack (one-off script implementation) as an alternative to the standard Python List implementation.
lifo = [] # Empty lifo variable list.

lifo.append('First')
lifo.append('Second')
lifo.append('Third')

def appendMain():
    print(lifo.pop()) # Each element of the list is dequeued using the same function as .pop() - Third is dequeued and iterated.
    print(lifo.pop()) # Second is dequeued and iterated.
    print(lifo.pop() + "\n") # First is dequeued and iterated.

appendMain() # Def caller function for testing out our alternative lifo queue implementation.