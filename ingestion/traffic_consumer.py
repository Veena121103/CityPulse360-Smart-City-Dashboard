from kafka import KafkaConsumer
import json

# Connect to Kafka
consumer = KafkaConsumer(
    'traffic-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='traffic-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening to traffic topic...")

# Read messages continuously
for message in consumer:

    data = message.value

    print(f"Received: {data}")