import matplotlib.pyplot as plt

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', color='blue', linestyle='-')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()










