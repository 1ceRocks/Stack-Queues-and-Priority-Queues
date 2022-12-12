# Handling Corner Cases in the Priority Queues
# ----------------------------------------------------------------

# This special program is used to check whether the priority has duplicates for a given value which corresponds to equal priorities. With the help of lexicographic order (which is a bit inconsistent since it doesn't support any comparison operators), it can resolve the comparison problem by engaging the value in the string; hence, for example the alphabetical order for the first letter is defined. Therefore, the queue should sort them by their insertion order.

# Imported data class module and class to represent messages in the queue.
from dataclasses import dataclass

@dataclass
class Message:
    event: str