import matplotlib.pyplot as plt
# Step Plot
x = [1, 2, 3, 4, 5]
y3 = [2, 5, 3, 7, 6]
plt.figure(figsize=(6,4))
plt.step(x, y3, where='mid', color='purple', linewidth=2)
plt.title("Step Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()