# Consumer Kafka Python 3 File

# * Naturally, we have only begun to scrape the surface of what these potent message brokers are capable of. Our objective in reading this part was to gain a fast overview and a place to start in case we wanted to further investigate them.

# * Essentially constructor of Kafka Python 3 Message one or more consumer classes that we are interested in reading from here.
from kafka3 import KafkaConsumer

# * The constructor of the consumer now selects one or more subjects in which the program could be interested.
consumer = KafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")