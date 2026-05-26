import pandas as pd

print("Loading complaints dataset...")

# Load dataset
df = pd.read_csv("data/NYC311data.csv")

print("Dataset loaded successfully!")

# Print columns
print(df.columns)

# Select useful columns
df = df[
    [
        "Created Date",
        "Complaint Type",
        "Borough",
        "Status"
    ]
]

# Remove null values
df = df.dropna()

# Rename columns
df.columns = [
    "timestamp",
    "complaint_type",
    "borough",
    "status"
]

# Keep first 5000 rows
df = df.head(5000)

# Save cleaned dataset
df.to_csv("data/complaints_cleaned.csv", index=False)

print("Complaints dataset cleaned successfully!")