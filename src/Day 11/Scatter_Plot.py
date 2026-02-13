import matplotlib.pyplot as plt
# Scatter Plot
x = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]
plt.figure(figsize=(6,4))
plt.scatter(x, y2, color='red', s=80)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()