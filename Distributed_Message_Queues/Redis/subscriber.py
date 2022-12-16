# You establish a connection to a nearby Redis server instance and start broadcasting messages on the chat channel right away. Redis will construct the channels for you, so you don't need to. There is an additional step needed to subscribe to a channel, which is to create the PubSub object on which to use the .subscribe() function.

# * Importing redis module to access memory key-value data cache between a traditional SQL database and a server.
import redis

# A subscriber now receives messages as Python dictionaries with few information, allowing them to determine how to handle it. The identical message will now be delivered to every active subscriber on a channel if there are several entities. Messages, on the other hand, are not persistent by default.
with redis.Redis() as client:
    pubsub = client.pubsub()
    pubsub.subscribe("chatroom")
    for message in pubsub.listen():
        if message["type"] == "message":
            body = message["data"].decode("utf-8")
            print(f"Got message: {body}")