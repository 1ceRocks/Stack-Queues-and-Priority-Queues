# A message broker typically perpetrates its own infrastructure to decouple application components from distributed systems with a lot of moving parts. It has its own pros and cons.

# One of the most well-known open source message brokers, RabbitMQ, allows us to route messages from producers to consumers in a number of different ways. Running a temporary Docker container allows us to quickly launch a new RabbitMQ broker without having to install it on our computer.
# Once it has begun, we may access it using localhost and the standard port 5672. The Pika library is advised by the official documentation for connecting to a RabbitMQ instance in Python.

# The Pika library is a Python wrapper for the popular RabbitMQ message broker.
import pika