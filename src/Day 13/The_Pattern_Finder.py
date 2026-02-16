import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("housing.csv")

# Generate correlation matrix
corr = df.corr(numeric_only=True)
print(corr)

# Plot correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Find highly correlated pairs
print("\nHighly correlated variables (> 0.8):")
for i in corr.columns:
    for j in corr.columns:
        if i != j and abs(corr.loc[i, j]) > 0.8:
            print(i, "and", j, "=", corr.loc[i, j])

# Boxplot to detect outliers
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Price"])
plt.title("Outliers in Price")
plt.show()
