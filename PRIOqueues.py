# Priority Queues Python File
# In this file, we need to create a different hierarchy for each process as the concept program subsides with priority queues. There is also an insertion order for us to determine on which new element is labeled for dequeueing. It's like removing the element from the highest priority as first iteration up to the least priority itself.

# For best manipulation efficiency, we will use the heap data structure algorithm.
from heapq import heappush # heapq module is used for O(log(n)) data volumes.
from heapq import heappop # Imported from heapq module.

fruits = [] # Fruits variable empty list.
# Non-empty heap function to maintain a heap invariant. It is not sorted but it would arrange everything on the right position.
heappush(fruits, 'peach')
heappush(fruits, 'avocado')
heappush(fruits, 'strawberry')

print(f"\n{fruits}\n") # Printing out the output for the program.

fruitpop = heappop(fruits) # Created a new variable to hold the function heappop().

print(fruitpop + "\n") # Using heappop will always get the first element while the remaining elements in the list might shuffle a little bit.

print(f"{fruits}\n") # The list is still in the right position when avocado is called out and dequeued. The lower unicode from Python to compare two string objects by value will reorder the words position from the list.

# # Note that the heap compares elements by value rather than their priority. It is like a lot of Python tuple function.
# player1 = ('Carlos', 'Christian', 40)
# player2 = ('Carlos', 'Fidel', 40)
# player3 = ('Carlos', 'Fidel', 14)

# if player1 < player2:
#     print("True")
# elif player2 < player3:
#     print("False")