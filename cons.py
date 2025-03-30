from time import sleep

from confluent_kafka import Consumer, KafkaException


# creating the consumer
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092', # the param bootstrap.servers is the configuratin used by both producers and consumers, it contains the list of brokers # noqa
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})


# subscribing our consumer to the topic that we created in producer.py
consumer.subscribe(['my-topic'])


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        elif msg.error():
            raise KafkaException(msg.error())
        print(f'Received the message: {msg.value().decode("utf-8")}')
        sleep(6)
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
