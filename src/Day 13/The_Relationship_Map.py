import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load dataset
df = pd.read_csv("housing.csv")

# 1. Distribution: Histogram + KDE
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()

# Skewness & Kurtosis
price_skew = skew(df["Price"])
price_kurt = kurtosis(df["Price"])

print("\n--- Distribution Statistics ---")
print("Skewness:", price_skew)
print("Kurtosis:", price_kurt)


# 2. Count Plot (Categorical)
plt.figure(figsize=(8,5))
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()

# 3. Scatter Plot (Interaction)
plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("SquareFootage vs Price")
plt.show()

# 4. Boxplot (City vs Price)
plt.figure(figsize=(8,5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price by City")
plt.show()
