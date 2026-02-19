# Import required libraries
import numpy as np                  
import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               

# Set seed for reproducibility
np.random.seed(0)

# Step 1: Create a heavily skewed dataset
# (Using exponential distribution to simulate income)

population = np.random.exponential(scale=50000, size=100000)

# Optional: Visualize original skewed data
plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population Distribution (Right-Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# Step 2: Take 1000 samples of size 30 and compute means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)   
    sample_mean = np.mean(sample)                    
    sample_means.append(sample_mean)                 

# Convert to DataFrame
means_df = pd.DataFrame({"Sample_Means": sample_means})

# Step 3: Plot distribution of sample means
plt.figure()
sns.histplot(means_df["Sample_Means"], kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

# Print Mean and Standard Deviation of sample means
print("Mean of Sample Means:", means_df["Sample_Means"].mean())
print("Standard Deviation of Sample Means:", means_df["Sample_Means"].std())
