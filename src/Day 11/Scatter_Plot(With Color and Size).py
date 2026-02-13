import matplotlib.pyplot as plt
# Scatter Plot with Sizes and Colors
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 7, 6]
sizes = [50, 100, 200, 150, 80]
colors = ['red', 'green', 'blue', 'purple', 'orange']
plt.figure(figsize=(6,4))
plt.scatter(x, y, s=sizes, c=colors, alpha=0.6)
plt.title("Scatter with Colors and Sizes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()