# Que7) Using for loop, write and run a Python program to find factorial from 0 to 10

def factorial(n1):
    if n1 == 1:
       return n1
    else:
       return n1 * factorial(n1-1)

for i in range (1,11):
    factorial(i)
    print(f"The factorial of {i} is {factorial(i)}")

