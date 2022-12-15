# A multi-process queue is a two-way communication across more OS-level interface processes. The last time approach was strictly for I/O bound task scenarios, but this time, it uses the available computational power by running CPU-bound tasks on its multiple integrated CPU cores in parallel with Python. It takes advantage of the cloning the interpreter process. The Windows Operating System provides IPC (InterProcess Communication) layer for distributing data across these processes.

# Importing the concurrent.futures module to carefully switch the replaced import statements from threads to processes for a smoother communication between those two. It also parallelize the existing code rather than straightforward from the rest of the code that follows a standard interface.

# They all differ in the level of completeness. The JoinableQueue extends the multiprocessing.Queue class by adding .task_done() and .join() methods, allowing you to wait until all enqueued tasks have been processed. If you don’t need this feature, then use multiprocessing.Queue instead. SimpleQueue is a separate, significantly streamlined class that only has .get(), .put(), and .empty() methods.
# * FIFO queue variants in the multiprocessing modules:
# ? multiprocessing.Queue 
# ? multiprocessing.SimpleQueue 
# ? multiprocessing.JoinableQueue

# Processes and threads are different types of operating system processes, and often don't share memory regions unlike threads. Data must be marshaled and un-marshaled at both ends every time its pass a message from one process toa another.

# ! pickle module is a handy tool for data serialization in Python, but usually doesn't handle every data type and is relatively slow and insecure.


# * Importing the necessary module string for reversing an MD5 Hash on a Single Thread
import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase

# * A function that attempts to reverse an MD5 hash value given as the first parameter is defined inside the reverse_md5() parametric function. The function by default only takes into account text made up of six lowercase ASCII characters. By supplying two more optional options, you may alter the alphabet and the maximum length of the text that can be guessed.
def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in product(alphabet, repeat=length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

# * Using a Python timer to calculate the execution time of a sample MD5 hash value. Finding a combination that hashes to the given input can take a few seconds on an experienced desktop computer: 
def main():
    t1 = time.perf_counter()
    # Due to its MD5 digest matching your hard-coded hash value on line 18, the word "queue" is the solution.
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960")
    print(f"{text} (found in {time.perf_counter() - t1:.1f}s)")

if __name__ == "__main__":
    main()

# TODO: By breaking up the whole set of letter combinations into a few more manageable disjoint subsets, you wish to reduce the search space in each worker. The sets cannot overlap in order to prevent employees from wasting time on tasks that have previously been completed by another worker. You can supply a number of pieces equal to the number of CPU cores even though you don't know the size of each individual chunk.