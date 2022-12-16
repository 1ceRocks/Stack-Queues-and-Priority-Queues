# Consumer Python File
# The majority of the boilerplate code resembles your producer. However, since the consumer will continue to listen for messages forever, you do not need to create an explicit loop.

# TODO: Launch a few producers and consumers in different terminal tabs. Take note of what transpires if more than one consumer is connected to the broker or if the queue already contains some unconsumed messages when the first consumer connects to RabbitMQ.

# * Importing pika to supplement RabbitMQ message broker.
import pika

QUEUE_NAME = "mailbox"

def callback(channel, method, properties, body):
    message = body.decode("utf-8")
    print(f"Got message: {message}")

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(
        queue=QUEUE_NAME,
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()