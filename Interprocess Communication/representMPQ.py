# Multi Process Queue object to manage multiple processes in parallel and presenting them individually.

# * The successive chunk lengths are rounded, and those with different lengths end up being beautifully interleaved:
from multiprocess_queue import chunk_indices

print("")
for start, stop in chunk_indices(20, 6):
    print(len(r := range(start, stop)), r)
print("")

# The indices produced by dividing a total length of twenty into six pieces, for instance, alternate between having three and four items. Each worker will create its own chunk of letter combinations depending on the range of indices supplied in a dequeued task object in order to reduce the cost of data serialization across your processes.