# Heap Queues Python File
# In this file, doing heap data structure distinguish elements from their value, therefore their indexes are defined and positioned from maximum to minimum and dequeueing them are in the same order considering the corresponding parameter using tuple comparison.

# For best manipulation efficiency, we will use the heap data structure algorithm.
from heapq import heappush, heappop # heapq module is used for O(log(n)) data volumes.

fruits = [] # Fruits variable empty list.
# Non-empty heap function to maintain a heap invariant. It is not sorted but it would arrange everything on the right position.
heappush(fruits, 'peach')
heappush(fruits, 'avocado')
heappush(fruits, 'strawberry')

def mainFruits():
    print(f"\n{fruits}\n") # Printing out the output for the program.

    for elements in fruits:
        fruitpop = heappop(fruits) # Created a new variable to hold the function heappop().
        print(fruitpop + "\n") # Using heappop will always get the first element while the remaining elements in the list might shuffle a little bit.
        print(f"{fruits}\n") # The list is still in the right position when avocado is called out and dequeued. The lower unicode from Python to compare two string objects by value will reorder the words position from the list.
    print(elements + "\n")

mainFruits()

# Note that the heap compares elements by value rather than their priority. It is like a lot of Python tuple function.
player1 = ('Carlos', 'Christian', 40)
player2 = ('Carlos', 'Fidel', 40)
player3 = ('Carlos', 'Fidel', 14)

if player1 < player2: # Age comparison is nullified because the ordering is already unknown.
    print("True")
elif player2 < player3: # Age comparison is now considered.
    print("False") # This can't be printed out as the elif condition is not satisfied based on the tuple comparison value.