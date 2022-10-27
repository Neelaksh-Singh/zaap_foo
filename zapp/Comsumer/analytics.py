import json

from kafka import KafkaConsumer

# Gets data from transactional backend
ORDER_CONFIRMED_KAFKA_TOPIC = "confirmed_order"


consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

orders_counter = 0
revenue_so_far = 0

print("Waiting for daily analytics...")
while True:
    for message in consumer:
        print("Updating analytics..")

        # Consumes message from the transaction backend
        consumed_message = json.loads(message.value.decode())
        total_cost = float(consumed_message["total_cost"])

        # Updates the daily orders and total transaction so far 
        orders_counter += 1
        revenue_so_far += total_cost
        print(f"Orders so far today: {orders_counter}")
        print(f"Revenue so far today: {revenue_so_far}")