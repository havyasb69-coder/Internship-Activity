import numpy as np                  
import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               

np.random.seed(0)

# 1. Human Heights (Normal Distribution)
heights = np.random.normal(loc=170, scale=8, size=1000)

# 2. Household Incomes (Right-Skewed Distribution)
incomes = np.random.exponential(scale=50000, size=1000)

# 3. Easy Exam Scores (Left-Skewed Distribution)
scores = 100 - np.random.exponential(scale=10, size=1000)

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

for column in df.columns:
    
    plt.figure()                                  
    sns.histplot(df[column], kde=True)            
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
    
    mean_value = df[column].mean()                
    median_value = df[column].median()            
    
    print(f"{column} Mean: {mean_value}")
    print(f"{column} Median: {median_value}")
    
    # Identify Skewness
    if mean_value > median_value:
        print("Observation: Right-Skewed (Mean > Median)")
    elif mean_value < median_value:
        print("Observation: Left-Skewed (Mean < Median)")
    else:
        print("Observation: Approximately Normal (Mean ≈ Median)")
    
    print("-" * 50)
