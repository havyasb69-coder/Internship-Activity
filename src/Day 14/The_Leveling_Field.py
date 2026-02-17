import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# create data with very different scales
salary = np.random.randint(20000, 200000, 200).reshape(-1, 1)

# standardization (mean 0, std 1)
std_scaler = StandardScaler()
salary_standard = std_scaler.fit_transform(salary)

# normalization (range 0–1)
mm_scaler = MinMaxScaler()
salary_normal = mm_scaler.fit_transform(salary)

# compare histograms
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.hist(salary, bins=20)
plt.title("Original")

plt.subplot(1,3,2)
plt.hist(salary_standard, bins=20)
plt.title("Standardized")

plt.subplot(1,3,3)
plt.hist(salary_normal, bins=20)
plt.title("Normalized")

plt.show()
