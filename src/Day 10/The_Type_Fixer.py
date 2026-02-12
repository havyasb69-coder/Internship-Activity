import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Check initial data types
print("\nInitial data types:")
print(df.dtypes)
print("Before Removing $ symbol and convert Price to float\n")
print(df["Price"])

# Remove $ symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
print("\nAfter removing $ symbol and convert Price to float")
print(df["Price"])

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check updated data types
print("\nUpdated data types:")
print(df.dtypes)
