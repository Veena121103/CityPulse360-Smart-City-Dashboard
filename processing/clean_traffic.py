import pandas as pd

print("Loading traffic dataset...")

# Load dataset
df = pd.read_csv("data/Metro_Interstate_Traffic_Volume.csv")

print("Dataset loaded successfully!")

# Select important columns
df = df[
    [
        "date_time",
        "traffic_volume",
        "temp",
        "weather_main",
        "weather_description"
    ]
]

# Remove null values
df = df.dropna()

# Rename columns
df.columns = [
    "timestamp",
    "traffic_volume",
    "temperature",
    "weather_main",
    "weather_description"
]

# Create congestion level
def congestion_level(volume):

    if volume < 2000:
        return "Low"

    elif volume < 5000:
        return "Medium"

    else:
        return "High"

df["congestion_level"] = df["traffic_volume"].apply(congestion_level)

# Keep only first 5000 rows
df = df.head(5000)

# Save cleaned dataset
df.to_csv("data/traffic_cleaned.csv", index=False)

print("Traffic dataset cleaned successfully!")