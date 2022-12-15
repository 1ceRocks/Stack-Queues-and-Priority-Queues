# A multi-process queue is a two-way communication across more OS-level interface processes. The last time approach was strictly for I/O bound task scenarios, but this time, it uses the available computational power by running CPU-bound tasks on its multiple integrated CPU cores in parallel with Python. It takes advantage of the cloning the interpreter process. The Windows Operating System provides IPC (InterProcess Communication) layer for distributing data across these processes.

# Importing the concurrent.futures module to carefully switch the replaced import statements from threads to processes for a smoother communication between those two. It also parallelize the existing code rather than straightforward from the rest of the code that follows a standard interface.

# They all differ in the level of completeness. The JoinableQueue extends the multiprocessing.Queue class by adding .task_done() and .join() methods, allowing you to wait until all enqueued tasks have been processed. If you don’t need this feature, then use multiprocessing.Queue instead. SimpleQueue is a separate, significantly streamlined class that only has .get(), .put(), and .empty() methods.
# * FIFO queue variants in the multiprocessing modules:
# ? multiprocessing.Queue 
# ? multiprocessing.SimpleQueue 
# ? multiprocessing.JoinableQueue

# Processes and threads are different types of operating system processes, and often don't share memory regions unlike threads. Data must be marshaled and un-marshaled at both ends every time its pass a message from one process toa another.

# ! pickle module is a handy tool for data serialization in Python, but usually doesn't handle every data type and is relatively slow and insecure.

# TODO: Before parallelizing the computation, let's focus on implementing a single-threaded version of the algorithm and measuring the execution time against some test input. Create a new Python module named multiprocess_queue and place the following code in it: