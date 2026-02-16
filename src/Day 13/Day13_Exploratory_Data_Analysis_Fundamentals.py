import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

# Univariate Analysis
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.show()

sns.boxplot(x=df['Salary'])
plt.title("Salary Boxplot")
plt.show()

print(df['Gender'].value_counts())

# Bivariate Analysis
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Age vs Salary")
plt.show()

sns.boxplot(x='Gender', y='Salary', data=df)
plt.title("Gender vs Salary")
plt.show()

# Correlation Analysis
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
