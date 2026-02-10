
try:
    with open(input("Enter the filename: "), "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.") 