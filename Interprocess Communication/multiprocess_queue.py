# A multi-process queue is a two-way communication across more OS-level interface processes. The last time approach was strictly for I/O bound task scenarios, but this time, it uses the available computational power by running CPU-bound tasks on its multiple integrated CPU cores in parallel with Python. It takes advantage of the cloning the interpreter process. The Windows Operating System provides IPC (InterProcess Communication) layer for distributing data across these processes.

# Importing the concurrent.futures module to carefully switch the replaced import statements from threads to processes for a smoother communication between those two. It also parallelize the existing code rather than straightforward from the rest of the code that follows a standard interface.

# They all differ in the level of completeness. The JoinableQueue extends the multiprocessing.Queue class by adding .task_done() and .join() methods, allowing you to wait until all enqueued tasks have been processed. If you don’t need this feature, then use multiprocessing.Queue instead. SimpleQueue is a separate, significantly streamlined class that only has .get(), .put(), and .empty() methods.
# * FIFO queue variants in the multiprocessing modules:
# ? multiprocessing.Queue 
# ? multiprocessing.SimpleQueue 
# ? multiprocessing.JoinableQueue
