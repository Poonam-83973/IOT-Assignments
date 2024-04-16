# Que 1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length = int(input("Enter the length of the ractangle: "))
breadth = int(input("Enter the breadth of the ractangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"The area of rectangle is : {area}")
print(f"The perimeter of rectangle is : {perimeter}")