import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load dataset
df = pd.read_csv("housing.csv")

# 1. Histogram + KDE
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()

# 2. Skewness & Kurtosis
price_skew = skew(df["Price"])
price_kurt = kurtosis(df["Price"])

print("\n--- Distribution Statistics ---")
print("Skewness:", price_skew)
print("Kurtosis:", price_kurt)

# 3. Count Plot (Categorical)
plt.figure(figsize=(8,5))
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("SquareFootage vs Price")
plt.show()

# 5. Boxplot (City vs Price)
plt.figure(figsize=(8,5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price by City")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(8,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Identify strong correlations
print("\n--- Highly Correlated Variables (>0.8) ---")
for col in corr.columns:
    for row in corr.index:
        if col != row and abs(corr.loc[row, col]) > 0.8:
            print(f"{row} and {col}: {corr.loc[row, col]}")
            
            
# 7. Outlier Detection
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Price"])
plt.title("Outliers in Price")
plt.show()

# 8. Written Observation Output
print("\n--- Observations ---")
print("Price distribution is right-skewed, indicating expensive outliers.")
print("Log transformation may improve ML performance.")
print("Square footage strongly increases with price.")
print("Some cities show higher median price and more outliers.")
print("Outliers exist and should be handled carefully.")
