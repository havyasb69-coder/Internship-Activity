import calc_rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))  

area, perimeter = calc_rectangle.calc_rectangle(length, width)
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)