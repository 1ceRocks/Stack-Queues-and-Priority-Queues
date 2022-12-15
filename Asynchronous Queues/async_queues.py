# Asynchronous operation queues are not supported by default in live production such as the data on the network, the file system, or a database. The programming concept comes into play. It behaves differently; it also takes one execution at a time. But the system may not wait to finish the execution to move on next step.

# In a synchronous environment, a program execution follows a set of operations sequentially. The execution flow will start processing a step and wait for it to return a result before proceeding to the next one. With asynchronous programming, we can use the lag time required by the operation to process and return a result to continue processing other tasks. This slows down the program as it is forced to stop and wait for something to finish. Many processors are available in the system, so it is a waste of resources to do other tasks rather than the ideal sit.

# Necessary libraries for parallel execution are defined in the following modules that can be used.
# aiohttp - to fetch data asynchronously
# beautifulsoup4 - to parse HTML Hyperlinks

# Layout for the web crawler.

# The asyncio module provides tons of asynchronous counterparts to queues from the threading module that would be useful for coroutine functions on a single thread.
import aiohttp, argparse, asyncio
from collections import Counter

# TODO: pass the main() coroutine to asyncio.run() so that it can perform on the default event loop.
async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()