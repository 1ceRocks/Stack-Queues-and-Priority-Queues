# The thread safe queues is a simultaneous, non-blocking operation cue of multithreaded program that executes more than one flow of execution. By the help of Python language, it provides a few synchronized queue types that we can safely use on multiple threads to facilitate communication between them. Beyond being a valuable algorithmic tool, queues can help abstract away concurrent access to a shared resource.

# We're going to implement a classic multi-producer, multi-consumer problem using this Python program. It usually visualizes / represents a command-line interface script that lets us decide on the number of producers and consumers, their relative speed rates, and the type of queue:

# Importing the necessary module and queue classes into the global namespace.
import argparse, threading
from queue import LifoQueue, PriorityQueue, Queue
from random import randint
from time import sleep

# Dictionary maps queue names to their respective classes, which we call to create a new queue instance based on the value of a command-line argument.
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue,
}

# The main() function is the entry point for the command-line interface. It takes a command-line argument and returns a queue instance. 
def main(args):
    buffer = QUEUE_TYPES[args.queue]()

# Receives the parsed arguments supplied by parse_args() that we defined.
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queue", choices=QUEUE_TYPES, default="fifo")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--producer-speed", type=int, default=1)
    parser.add_argument("-cs", "--consumer-speed", type=int, default=1)
    return parser.parse_args()

# TODO: support multiple producers and consumers.
if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass

# Textual codes that Rich will eventually replace with the corresponding emoji glyphs. For example, :balloon: will render as 🎈. The producer and consumer will share a wealth of attributes and behaviors, which you can encapsulate in a common base class:
PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)

# The worker class extends the threading.Thread class and configures itself as a daemon thread so that its instances won’t prevent your program from exiting when the main thread finishes, for example, due to a keyboard interrupt signal. A worker object expects the speed rate to work with and a buffer queue to put finished products into or get them from.
class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon = True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0
    
    # The .state property returns a string with either the product’s name and the progress of work or a generic message indicating that the worker is currently idle.
    @property
    def state(self):
        if self.working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: Idle"

    # The .simulate_idle() method resets the state of a worker thread and goes to sleep for a few randomly chosen seconds.
    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))