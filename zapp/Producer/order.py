import json
import time
import random
from food_item import foodGenerator

from kafka import KafkaProducer

# Setting the topic and order limit
ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 20000

# Initializing producer 
producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("!! Welcome to zaap_foo !!")
print("One unique order will be generated in 5 seconds")
time.sleep(5)

# Time to produce our orders
for i in range(1, ORDER_LIMIT):
    tot_food_item = random.randint(1,5)
    order = foodGenerator(tot_food_items=tot_food_item)
    data = {
        "order_id": i,
        "user_id": f"usId_{i}",
        "total_cost": i * 5,
        "items": order,
    }

    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(0.2)