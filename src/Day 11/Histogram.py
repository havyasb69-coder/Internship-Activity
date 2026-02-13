import matplotlib.pyplot as plt
# Histogram
data = [5, 7, 8, 9, 4, 7, 8, 6, 5, 7, 9]
plt.figure(figsize=(6,4))
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()