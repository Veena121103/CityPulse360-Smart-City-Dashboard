import pandas as pd

print("Loading accident dataset...")

# Read only important columns
df = pd.read_csv(
    "data/US_Accidents_March23.csv",
    usecols=[
        "ID",
        "Severity",
        "Start_Time",
        "Start_Lat",
        "Start_Lng",
        "Distance(mi)",
        "Traffic_Signal",
        "Sunrise_Sunset"
    ]
)

print("Dataset loaded successfully!")

# Remove missing values
df = df.dropna()

# Keep only first 5000 rows
df = df.head(5000)

# Save cleaned dataset
df.to_csv("data/accidents_cleaned.csv", index=False)

print("Accident dataset cleaned successfully!")