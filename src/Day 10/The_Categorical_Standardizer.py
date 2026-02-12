import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Check messy values first
print("Before cleaning:")
print(df["Location"].unique())

# Remove spaces + standardize casing
df["Location"] = df["Location"].str.strip().str.title()

# Verify fix
print("\nAfter cleaning:")
print(df["Location"].unique())
