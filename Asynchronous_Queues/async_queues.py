# Asynchronous operation queues are not supported by default in live production such as the data on the network, the file system, or a database. The programming concept comes into play. It behaves differently; it also takes one execution at a time. But the system may not wait to finish the execution to move on next step.

# In a synchronous environment, a program execution follows a set of operations sequentially. The execution flow will start processing a step and wait for it to return a result before proceeding to the next one. With asynchronous programming, we can use the lag time required by the operation to process and return a result to continue processing other tasks. This slows down the program as it is forced to stop and wait for something to finish. Many processors are available in the system, so it is a waste of resources to do other tasks rather than the ideal sit.

# Necessary libraries for parallel execution are defined in the following modules that can be used.
# aiohttp - to fetch data asynchronously
# beautifulsoup4 - to parse HTML Hyperlinks

# Layout for the web crawler.

# The asyncio module provides tons of asynchronous counterparts to queues from the threading module that would be useful for coroutine functions on a single thread.
import aiohttp, argparse, asyncio
from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Defines a counter on the visited links on the HTML hyperlinks being parsed. It also passes the coroutine execution to asyncio.run() for it to have a default event loop session. The coroutine then would pass back and display the list of links sorted by the number of visits in descending order.
async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()

# The 2 define block codes [parse_args() and display(links)]Coroutine receives few command-line interface and returns them with parsed arguments.
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")

# This counter is used internally by the asyncio module to track the number of concurrent requests that are queued to the same page. It also acts as the global workspace for running through parallel processes.
if __name__ == "__main__":
    asyncio.run(main(parse_args()))

# This will only inherit and return an HTML content from the .content_type operator tag.
async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == 'text/html':
            return await response.text()

# TODO: We'll now implement an extracted links from the HTML document and skip the inline JavaScript with the use of href() attribute, which will incorporate a relative path with the current global machine URL.