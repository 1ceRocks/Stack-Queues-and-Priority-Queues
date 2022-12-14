# The thread safe queues is a simultaneous, non-blocking operation cue of multithreaded program that executes more than one flow of execution. By the help of Python language, it provides a few synchronized queue types that we can safely use on multiple threads to facilitate communication between them. Beyond being a valuable algorithmic tool, queues can help abstract away concurrent access to a shared resource.

# We're going to implement a classic multi-producer, multi-consumer problem using this Python program. It usually visualizes / represents a command-line interface script that lets us decide on the number of producers and consumers, their relative speed rates, and the type of queue:

# Importing the necessary module and queue classes into the global namespace.
import argparse, threading
from queue import LifoQueue, PriorityQueue, Queue
from random import choice, randint
from time import sleep
from itertools import zip_longest

# For PriorityQueue instances
from dataclasses import dataclass, field
from enum import IntEnum

# Expanding the collapsible section of the presentation based on the Rich library.
from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

# Dictionary maps queue names to their respective classes, which we call to create a new queue instance based on the value of a command-line argument.
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue,
}


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

# To use a synchronized priority queue or a heap, you’ll need to make a few adjustments in your code. First of all, you’re going to need a new kind of product that has an associated priority, so define two new data types:
# To represent products, we use a data class with a customized string representation and ordering enabled, but we're careful not to compare the products by their label. In this case, we expect the label to be a string, but generally, it could be any object that might not be comparable at all. We also define an enum class with known priority values and three products with descending priorities from highest to lowest.
@dataclass(order=True)
class Product:
    priority: int
    label: str = field(compare=False)

    def __str__(self):
        return self.label

class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

PRIORITIZED_PRODUCTS = (
    Product(Priority.HIGH, ":1st_place_medal:"),
    Product(Priority.MEDIUM, ":2nd_place_medal:"),
    Product(Priority.LOW, ":3rd_place_medal:"),
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

    # The .simulate_work() picks a random delay in seconds adjusted to the worker’s speed and progresses through the work.
    def simulate_work(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 15 // self.speed)
        for _ in range(100):
            sleep(delay / 100)
            self.progress += 1

# The code below defines a view that renders the current state of your producers, consumers, and the queue ten times a second:
# Notice the use of structural pattern matching to set the title and products based on the queue type. We'll create an instance of the view and call its .animate() method once the producers and consumers are in place.
class View:
    def __init__(self, buffer, producers, consumers):
        self.buffer = buffer
        self.producers = producers
        self.consumers = consumers

    def animate(self):
        with Live(
            self.render(), screen=True, refresh_per_second=10
        ) as live:
            while True:
                live.update(self.render())

    def render(self):

        match self.buffer:
            case PriorityQueue():
                title = "Priority Queue"
                products = map(str, reversed(list(self.buffer.queue)))
            case LifoQueue():
                title = "Stack"
                products = list(self.buffer.queue)
            case Queue():
                title = "Queue"
                products = reversed(list(self.buffer.queue))
            case _:
                title = products = ""

        rows = [
            Panel(f"[bold]{title}:[/] {', '.join(products)}", width=82)
        ]
        pairs = zip_longest(self.producers, self.consumers)
        for i, (producer, consumer) in enumerate(pairs, 1):
            left_panel = self.panel(producer, f"Producer {i}")
            right_panel = self.panel(consumer, f"Consumer {i}")
            rows.append(Columns([left_panel, right_panel], width=40))
        return Group(*rows)

    def panel(self, worker, title):
        if worker is None:
            return ""
        padding = " " * int(29 / 100 * worker.progress)
        align = Align(
            padding + worker.state, align="left", vertical="middle"
        )
        return Panel(align, height=5, title=title)

# The .run() method is where all the magic happens. A producer works in an infinite loop, choosing a random product and simulating some work before putting that product onto the queue, called a buffer. It then goes to sleep for a random period, and when it wakes up again, the process repeats.
class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products

    def run(self):
        while True:
            self.product = choice(self.products)
            self.simulate_work()
            self.buffer.put(self.product)
            self.simulate_idle()

# A consumer is very similar, but even more straightforward than a producer:
# It also works in an infinite loop, waiting for a product to appear in the queue. The .get() method is blocking by default, which will keep the consumer thread stopped and waiting until there’s at least one product in the queue. This way, a waiting consumer won’t be wasting any CPU cycles while the operating system allocates valuable resources to other threads doing useful work.
class Consumer(Worker):
    def run(self):
        while True:
            self.product = self.buffer.get()
            self.simulate_work()
            self.buffer.task_done()
            self.simulate_idle()
            
# The main() function is the entry point for the command-line interface. It takes a command-line argument and returns a queue instance. 
def main(args):
    buffer = QUEUE_TYPES[args.queue]()
    products = PRIORITIZED_PRODUCTS if args.queue == "heap" else PRODUCTS
    producers = [
        Producer(args.producer_speed, buffer, PRODUCTS)
        for _ in range(args.producers)
    ]
    consumers = [
        Consumer(args.consumer_speed, buffer) for _ in range(args.consumers)
    ]

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()

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