import matplotlib.pyplot as plt
# 3. Bar Chart
categories = ['A', 'B', 'C']
values = [11, 20, 15]
plt.figure(figsize=(6,4))
plt.bar(categories, values, color='orange')
plt.title("Bar Chart")
plt.show()