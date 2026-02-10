a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
operation = input("Enter operation (+, -, *, /): ") 
if operation == '+':
    result = a + b          
elif operation == '-':
    result = a - b                  
elif operation == '*':      
    result = a * b
elif operation == '/':  
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"     
print("Result:", result)    
    