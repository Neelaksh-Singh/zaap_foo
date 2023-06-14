import json
import matplotlib.pyplot as plt
from kafka import KafkaConsumer

# Gets data from transactional backend
ORDER_CONFIRMED_KAFKA_TOPIC = "confirmed_order"

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:29092"
)

orders_counter = 0
revenue_so_far = 0

# Initialize lists to store data for plotting
orders = []
revenues = []

# Create a figure and axis for the plot
fig, ax = plt.subplots()

plt.ion()  # Enable interactive mode for real-time updates

# Plot settings
plt.title("Real-time Daily Analytics")
plt.xlabel("Time (Orders)")
plt.ylabel("Revenue")

# Set initial y-axis limits for better visibility
ax.set_ylim(0, 1.1 * revenue_so_far)

print("Waiting for daily analytics...")
while True:
    for message in consumer:
        print("Updating analytics...")

        # Consumes message from the transaction backend
        consumed_message = json.loads(message.value.decode())
        total_cost = float(consumed_message["total_cost"])

        # Updates the daily orders and total transaction so far
        orders_counter += 1
        revenue_so_far += total_cost

        # Append data to lists for plotting
        orders.append(orders_counter)
        revenues.append(revenue_so_far)

        # Clear the previous plot and plot the updated data
        ax.clear()
        ax.plot(orders, revenues, color='b')

        # Add performance metrics to the plot
        ax.annotate(
            f"Orders: {orders_counter}",
            xy=(orders_counter, revenue_so_far),
            xytext=(orders_counter, revenue_so_far + 0.05 * revenue_so_far),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            fontsize=8,
            ha='center'
        )
        ax.annotate(
            f"Revenue: ${revenue_so_far:.2f}",
            xy=(orders_counter, revenue_so_far),
            xytext=(orders_counter, revenue_so_far - 0.05 * revenue_so_far),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            fontsize=8,
            ha='center'
        )

        # Display Kafka metrics
        ax.annotate(
            f"Kafka: {message.topic}, Partition: {message.partition}, Offset: {message.offset}",
            xy=(orders_counter, revenue_so_far),
            xytext=(orders_counter, revenue_so_far + 0.1 * revenue_so_far),
            fontsize=8,
            ha='center'
        )

        # Adjust y-axis limits based on the updated revenue
        ax.set_ylim(0, 1.1 * revenue_so_far)

        # Display the plot
        plt.draw()
        plt.pause(0.001)

        print(f"Orders so far today: {orders_counter}")
        print(f"Revenue so far today: {revenue_so_far:.2f}")
