import json

from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC = "confirmed_order"


consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

# Keeps track of unique emails for the day
emails_sent_so_far = set()

print("Waiting for transactions to start ...")
while True:
    for message in consumer:
        
        # Starts to get completed transactional data
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        
        print(f"Sending email to {customer_email} ")
        emails_sent_so_far.add(customer_email)
        print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")