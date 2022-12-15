# Asynchronous operation queues are not supported by default in live production such as the data on the network, the file system, or a database. The programming concept comes into play. It behaves differently; it also takes one execution at a time. But the system may not wait to finish the execution to move on next step.

# In a synchronous environment, a program execution follows a set of operations sequentially. The execution flow will start processing a step and wait for it to return a result before proceeding to the next one. With asynchronous programming, we can use the lag time required by the operation to process and return a result to continue processing other tasks. This slows down the program as it is forced to stop and wait for something to finish. Many processors are available in the system, so it is a waste of resources to do other tasks rather than the ideal sit.

# * Necessary libraries for parallel execution are defined in the following modules that can be used.
# ? aiohttp - to fetch data asynchronously
# ? beautifulsoup4 - to parse HTML Hyperlinks

# Layout for the web crawler.

# The asyncio module provides tons of asynchronous counterparts to queues from the threading module that would be useful for coroutine functions on a single thread.
# These modules are supplemented with later commits to satisfy data type algorithms that would otherwise be impossible to implement in the future.
import aiohttp, argparse, asyncio, sys
from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import NamedTuple

# * Unpacking its individual resources on the await queue.get() method inside the def worker() function after dequeueing the component. The variable depth value when not specified, always defaults to one.
class Job(NamedTuple):
    url: str
    depth: int = 1

# * Defines a counter on the visited links on the HTML hyperlinks being parsed. It also passes the coroutine execution to asyncio.run() for it to have a default event loop session. The coroutine then would pass back and display the list of links sorted by the number of visits in descending order.
async def main(args):
    session = aiohttp.ClientSession()
    # TODO: (PLACEMENT of Modification) Create an instance of the asynchronous queue and pass it to the artificial programmed workers. main() coroutine will supplement lines of codes that creates queues and asynchronous tasks to each worker with unique identifier tags that would differentiate inside the log messages. A necessary session, aiohttp library is required for queue instance, the counter for visits in a URL link, and its hits for maximum depth allowed.
    # ! print() function can be used to display the output because the program utilizes the single-thread CPU queue.
    try:
        links = Counter()
        # ? -- area for modification --
        display(links)
    finally:
        await session.close()

# * A depth parameter specified the number of links to be displayed. The artificial programmed worker also depends on this depth to stop crawling recursively. The worker reads and supplements the value of hits associated with URL visits; additionally, when it doesn't exceed its maximum allowed depth on the depth of URL, the worker iterates over its links and fetch the HTML content that the URL points.
async def worker(worker_id, session, queue, links, max_depth):
    print(f"[{worker_id} starting]", file=sys.stderr)
    while True:
        url, depth = await queue.get()
        links[url] += 1
        # ? to avoid an unusual error when the worker is already running with the current job depth in the queue acting as producer and consumer, the try... finally handles to avoid a deadlock. This would be crucial as to when the worker doesn't have any programmed exceptions, a possibility would occur that stops accepting new jobs. 
        try:
            if depth <= max_depth:
                print(f"[{worker_id} {depth=} {url=}]", file=sys.stderr)
                # ? the assignment operator ":=" (pseudocode language) lets an HTTP response await, check if the content was returned, and assign its result on the html variable as a single expression.
                if html := await fetch_html(session, url):
                    for link_url in parse_links(url, html):
                        await queue.put(Job(link_url, depth + 1))
        except aiohttp.ClientError:
            print(f"[{worker_id} failed at {url=}]", file=sys.stderr)
        finally:
            queue.task_done()

# * The 2 define block codes [parse_args() and display(links)]Coroutine receives few command-line interface and returns them with parsed arguments.
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")

# * This counter is used internally by the asyncio module to track the number of concurrent requests that are queued to the same page. It also acts as the global workspace for running through parallel processes.
if __name__ == "__main__":
    asyncio.run(main(parse_args()))

# * This will only inherit and return an HTML content from the .content_type operator tag.
async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == 'text/html':
            return await response.text()

# * Inline JavaScript that joins a relative path with the current global machine URL.
def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript:"):
            yield urljoin(url, href)