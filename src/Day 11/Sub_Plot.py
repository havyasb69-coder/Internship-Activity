import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [10, 8, 6, 4, 2]

fig, axs = plt.subplots(2, 2, figsize=(10, 6))

axs[0, 0].plot(x, y1, marker='o', color='blue')
axs[0, 0].set_title("Line Plot")

axs[0, 1].step(x, y2, where='mid', color='green')
axs[0, 1].set_title("Step Plot")

axs[1, 0].bar(x, y1, color='orange')
axs[1, 0].set_title("Bar Plot")

axs[1, 1].scatter(x, y2, color='red')
axs[1, 1].set_title("Scatter Plot")

plt.tight_layout()
plt.show()
