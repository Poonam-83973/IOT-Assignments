# Que 6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function 
#   accepts the number as an argument.

num = int(input("Enter number: "))

def factorial(n1):
    if n1 == 1:
       return n1
    else:
       return n1 * factorial(n1-1)

print(f"The factorial of {num} is {factorial(num)}")

