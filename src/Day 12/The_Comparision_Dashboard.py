import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Line plot data (example trend)
months = [1, 2, 3, 4, 5]
trend = [100, 200, 300, 250, 400]

plt.figure(figsize=(10, 4))

# Subplot 1: Bar chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

# Subplot 2: Line plot
plt.subplot(1, 2, 2)
plt.plot(months, trend)
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()
