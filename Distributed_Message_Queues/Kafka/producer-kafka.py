# Producer Kafka Python 3 File

# ? When Kafka and our client library have different versions, we could occasionally encounter problems. Kafka-python3, which is based on the Java client, is a Python library that appears to work with a more current version of Kafka. Our producer has the following options for communications on a certain subject:
from kafka3 import KafkaProducer

# * Because it provides a future object that we may await by invoking its blocking.get() function, the.send() method is asynchronous. On the consumer’s side, we'll be able to read the transmitted messages by iterating over the consumer:
producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )