from time import sleep

from datetime import datetime

from confluent_kafka import Producer


# just a function to handle the producer behavior

def delivery_message(err, msg):
    if err:
        print(f'An error occured see >>> {err}')
    print(f'Successfully sent the message >>> {msg.value().decode("utf-8")}')


# creating our producer

# we are using localhost:9092, but we can pass the addres of another broker

producer = Producer({'bootstrap.servers': 'localhost:9092'}) # 9092 is the default port for kafka # noqa


# creating a topic
topic = 'my-topic'

# now we are gonna produce our message
# the callback funcition is that one we wrote there above :)

while True:
    # creating a simple message
    message = f'Hello, it is {datetime.strftime(datetime.now(), "%H:%M%S")}'

    producer.produce(topic, message.encode('utf-8'), callback=delivery_message)
    producer.flush()

    sleep(3)
