import numpy as np                  
import pandas as pd                 

np.random.seed(0)

# Generate Sample Dataset 
data = np.random.normal(loc=1000, scale=200, size=1000)   

df = pd.DataFrame({"SAT_Score": data})                    

# Step 1: Calculate Mean (μ) and Standard Deviation (σ)
mu = df["SAT_Score"].mean()                               
sigma = df["SAT_Score"].std()                             

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

# Step 2: Create Z-score column
# Formula: Z = (x - μ) / σ
df["z_score"] = (df["SAT_Score"] - mu) / sigma

# Step 3: Identify Outliers where |Z| > 3

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)
print("\nNumber of Outliers:", len(outliers))
