import pandas as pd

products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])
laptop_price = products['Laptop']
first_two = products.iloc[:2]

print("Full Series:")
print(products)

print(f"\nPrice of Laptop : {laptop_price}")

print("\nFirst two products (positional slice):")
print(first_two)
