# You establish a connection to a nearby Redis server instance and start broadcasting messages on the chat channel right away. Redis will construct the channels for you, so you don't need to. There is an additional step needed to subscribe to a channel, which is to create the PubSub object on which to use the .subscribe() function.

# * Importing redis module to access memory key-value data cache between a traditional SQL database and a server.
import redis

# TODO: A subscriber receives messages as Python dictionaries with some information, allowing us to determine how to handle them. The identical message will be delivered to every active subscriber on a channel if there are several of them. Messages, on the other hand, are not persistent by default.