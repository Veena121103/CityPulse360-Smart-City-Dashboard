from kafka import KafkaProducer
import pandas as pd
import json
import time

# Kafka connection
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Load cleaned traffic dataset
df = pd.read_csv("data/traffic_cleaned.csv")

print("Starting traffic streaming...")

# Send rows one by one
for index, row in df.iterrows():

    data = row.to_dict()

    producer.send("traffic-topic", value=data)

    print(f"Sent: {data}")

    time.sleep(1)

print("Traffic streaming completed!")