import matplotlib.pyplot as plt
# Pie Chart
sizes = [20, 30, 25, 25]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()