from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv("data/aqi_cleaned.csv")

print("Starting AQI streaming...")

for index, row in df.iterrows():

    data = row.to_dict()

    producer.send("aqi-topic", value=data)

    print(f"Sent: {data}")

    time.sleep(1)

print("AQI streaming completed!")