import pandas as pd

print("Loading AQI dataset...")

# Load dataset
df = pd.read_csv("data/real_2016.csv")

print("Dataset loaded successfully!")

# Remove null values
df = df.dropna()

# Select useful columns
df = df[
    [
        "T",
        "TM",
        "Tm",
        "SLP",
        "PM 2.5"
    ]
]

# Rename columns
df.columns = [
    "temperature_avg",
    "temperature_max",
    "temperature_min",
    "sea_level_pressure",
    "pm25"
]

# Create AQI category
def pollution_level(pm):

    if pm < 50:
        return "Good"

    elif pm < 100:
        return "Moderate"

    else:
        return "Poor"

df["pollution_level"] = df["pm25"].apply(pollution_level)

# Keep first 5000 rows
df = df.head(5000)

# Save cleaned dataset
df.to_csv("data/aqi_cleaned.csv", index=False)

print("AQI dataset cleaned successfully!")