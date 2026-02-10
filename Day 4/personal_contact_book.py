contact = {"Havyas": 8088953488,"Bhavish": 9876543210,"Dilan":987123450}
print(contact)
contact.update({"Dilan": 9123456780})
print(contact)
print(contact["Havyas"])
print(contact.get("Rakshith", "Contact Not Found"))
for name,number in contact.items():
    print(f"Contact : {name} Phone : {number}")