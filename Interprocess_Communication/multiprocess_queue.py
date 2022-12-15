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
import argparse, multiprocessing, queue, time
from hashlib import md5
from itertools import product
from string import ascii_lowercase
from dataclasses import dataclass

# * Killing a Worker With the Posion Pill
POISON_PILL = None

# * For a specific index, we need to locate a letter combination or an n-tuple or m-set. You may create a new class that contains the combination's formula to make your life simpler:
class Combinations:
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length

    def __len__(self):
        return len(self.alphabet) ** self.length

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return "".join(
            self.alphabet[
                (index // len(self.alphabet) ** i) % len(self.alphabet)
            ]
            for i in reversed(range(self.length))
        )

# .__call__() is a special method that allows to call objects from our class from within a task. Because of this, when employees obtain certain responsibilities, they can refer to them as normal tasks.
@dataclass(frozen=True)
class Job:
    combinations: Combinations
    start_index: int
    stop_index: int

    def __call__(self, hash_value):
        for index in range(self.start_index, self.stop_index):
            text_bytes = self.combinations[index].encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

# The program will then be terminated early if the main process notices that one of the workers has added a reversed MD5 text to the output queue on a periodic basis. Since the employees are daemons, the primary procedure won't be slowed down. Also note that the input hash value is reversely stored by the workers.
class Worker(multiprocessing.Process):
    def __init__(self, queue_in, queue_out, hash_value):
        super().__init__(daemon=True)
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.hash_value = hash_value

    def run(self):
        while True:
            job = self.queue_in.get()
            # ? Each of our worker processes would have a separate instance of that object with its own unique identity if you utilized a custom object() instance declared as a global variable. When a sentinel object is enqueued by one worker, it will be deserialized into a whole new instance with a distinct identity from its global variable in another worker. As a result, you couldn't tell if there was a deadly pill in the line.
            if job is POISON_PILL:
                self.queue_in.put(POISON_PILL)
                break
            if plaintext := job(self.hash_value):
                self.queue_out.put(plaintext)
                break

# * At this stage, your employees interact with the main process in a two-way manner via the input and output queues. However, because the main process terminates without waiting for its daemon offspring to complete performing their duties, the application quits abruptly immediately after beginning.

# ? Appended and Modified some code from the original code above that was written before.
def main(args):
    t1 = time.perf_counter()

    queue_in = multiprocessing.Queue()
    queue_out = multiprocessing.Queue()

    workers = [
        Worker(queue_in, queue_out, args.hash_value)
        for _ in range(args.num_workers)
    ]

    # * The script is now finished and capable of both identifying a matched text and dealing with circumstances in which the MD5 hash value cannot be reversed. We'll run a few benchmarks in the part after this one to see whether the work put into this exercise was worthwhile.
    for worker in workers:
        worker.start()

    for text_length in range(1, args.max_length + 1):
        combinations = Combinations(ascii_lowercase, text_length)
        for indices in chunk_indices(len(combinations), len(workers)):
            queue_in.put(Job(combinations, *indices))
    
    queue_in.put(POISON_PILL)

    while any(worker.is_alive() for worker in workers):
        try:
            solution = queue_out.get(timeout=0.1)
            if solution:
                t2 = time.perf_counter()
                print(f"{solution} (found in {t2 - t1:.1f}s)")
                break
        except queue.Empty:
            pass
    else:
        print("Unable to find a solution")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("hash_value")
    parser.add_argument("-m", "--max-length", type=int, default=6)
    parser.add_argument(
        "-w",
        "--num-workers",
        type=int,
        default=multiprocessing.cpu_count(),
    )
    return parser.parse_args()

# * It produces tuples that may easily be used as input for the built-in range() method since they contain the start index of the current chunk and its last index raised by one.
def chunk_indices(length, num_chunks):
    start = 0
    while num_chunks > 0:
        num_chunks = min(num_chunks, length)
        chunk_size = round(length / num_chunks)
        yield start, (start := start + chunk_size)
        length -= chunk_size
        num_chunks -= 1

# * A function that attempts to reverse an MD5 hash value given as the first parameter is defined inside the reverse_md5() parametric function. The function by default only takes into account text made up of six lowercase ASCII characters. By supplying two more optional options, you may alter the alphabet and the maximum length of the text that can be guessed.
# def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
#     for length in range(1, max_length + 1):
#         for combination in product(alphabet, repeat=length):
#             text_bytes = "".join(combination).encode("utf-8")
#             hashed = md5(text_bytes).hexdigest()
#             if hashed == hash_value:
#                 return text_bytes.decode("utf-8")

# * Using a Python timer to calculate the execution time of a sample MD5 hash value. Finding a combination that hashes to the given input can take a few seconds on an experienced desktop computer:
#  
# This will comment line 34-41New code block will be laid out.
# def main():
#     t1 = time.perf_counter()
#     # Due to its MD5 digest matching your hard-coded hash value on line 18, the word "queue" is the solution.
#     text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960")
#     print(f"{text} (found in {time.perf_counter() - t1:.1f}s)")

# if __name__ == "__main__":
#     main()

# * Class in the MD5-reversing method and get rid of the "itertools.product" import declaration.
# ! Unfortunately, using pure Python to do some computations and replacing a built-in function developed in C makes the code an order of magnitude slower:
# Reverse md5() may now be deleted because it is no longer required because the method's body is very similar to it yet somewhat different.
# def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
#     for length in range(1, max_length + 1):
#         for combination in Combinations(alphabet, length):
#             text_bytes = "".join(combination).encode("utf-8")
#             hashed = md5(text_bytes).hexdigest()
#             if hashed == hash_value:
#                 return text_bytes.decode("utf-8")


# Each worker process will have a reference to both the output queue for the potential solution and the input queue with tasks to consume. Full-duplex communication, sometimes referred to as simultaneous two-way communication, is made possible by these references between the employees and the primary process. You extend the Process class, which has the well-known.run() function, exactly like a thread, to construct a worker process:

if __name__ == "__main__":
    main(parse_args())