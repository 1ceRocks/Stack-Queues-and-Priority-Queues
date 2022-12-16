# The name Redis, which stands for Remote Dictionary Server, really refers to a variety of things. It's an in-memory key-value data store that often serves as an incredibly quick cache between a server and a standard SQL database. It can function both as a publish-subscribe message broker and a persistent NoSQL database at the same time. With Docker, we may launch a local Redis server:

# Importing redis module to access memory key-value data cache between a traditional SQL database and a server.
import redis

# * It only takes a few lines of Python code to create a simple publisher:
with redis.Redis() as client:
    while True:
        message = input("Message: ")
        client.publish("chatroom", message)