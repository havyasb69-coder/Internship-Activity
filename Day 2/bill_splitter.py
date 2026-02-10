bill_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people to split the bill: "))
amount_per_person = bill_amount / num_people
type = type(amount_per_person)
print("type of bill_amount is:", type)
print(f"Each person should pay: Rupees {amount_per_person}")