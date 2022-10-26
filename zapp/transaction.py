import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

# This script acts both as the producer and the consumer
# It gets order from restuarents and returns confirmed orders
 
ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "confirmed_order"

# Consuming orders
consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

# Producing confirmed orders 
producer = KafkaProducer(bootstrap_servers="localhost:29092")


print("Bonjure! Welcome to zaap foods")
while True:
    for message in consumer:
        print("Ongoing transaction..")

        # Loading messages from kafka topic
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]

        # Pushing data into kafka topic
        data = {
            "customer_id": user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost
        }
        print("Transaction Successfull..")
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))