a = {"Apple" : "Fruit"}
print(type(a))
b = {1 : 2}
print(b)

# Dictionary Hands-on
student = {
    "Name" : "Havyas",
    "Age" : 23,
    "Courses" : "MCA",
}
print(student["Name"])
student["Age"] = 24
student["city"] = "Puttur"
print(student)


# Dictionary Methods and Iteration
marks = {
    "Maths" : 90,
    "Science" : 85,
    "English" : 88,
}
print(marks.get("Maths"))
marks.update({"English" : 92})
marks.update({"History" : 80})
print(marks.get("History", 0))  
for subject, score in marks.items():
    print(subject, score)  
marks.pop("Science")
print(marks)

#Retail store example
purchases = {
    "Alice" : 150,
    "Bob" : 200,
    "Charlie" : 300,
}

for customer, amount in purchases.items():
    print(f"{customer} purchases total ₹ {amount} of items")  
print(f"Total customers: {len(purchases)}")  

print("Customers Names:",list(purchases.keys()))
print("Purchase Amounts:",list(purchases.values()))
print("Alice's Purchase:",purchases.get("Alice",0))


#Input from user to create dictionary
num_items = int(input("Enter number of items to add to inventory: "))   
user_purchases = {}

for i in range(num_items):
    name = input("Enter customer name: ")
    amount = int(input("Enter purchase amount: "))
    user_purchases[name] = amount

    print("User Purchases Dictionary:", user_purchases)

top_customer = max(user_purchases, key=user_purchases.get)
print(f"Top Customer: {top_customer} with purchase amount ₹ {user_purchases[top_customer]}")
lowest_customer = min(user_purchases, key=user_purchases.get)
print(f"Lowest Customer: {lowest_customer} with purchase amount ₹ {user_purchases[lowest_customer]}")


#Sets 
numbers = {1, 2, 3, 4, 5, 5}
print(numbers)
numbers.add(6)
print(numbers) 

#Set Operations
A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print(3 in A)
