# Que 2] Write a program to accept a 4 digit number and
#       a. Display face value of each decimal digit
#       b. Display place value of each decimal digit
#       c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 
#          9361 output should be
#       a. 9 3 6 1
#       b. 9361 = 9 000 + 300 + 60 + 9
#       c. 1639

num1 = int(input("Enter the 4 digit number: "))
val1 = int(num1 % 10)
num1 = num1/10

val2 = int(num1 % 10)
num1 = num1/10

val3 = int(num1 % 10)
num1 = num1/10

val4 = int(num1 % 10)

print(f"The face value of each digit is :{val4} {val3} {val2} {val1}")
print(f"The place value of each decimal digit is: {val4*1000} + {val3*100} + {val2*10} +{val1*1}")
print(f"The reverse order of number  is :{val1} {val2} {val3} {val4}")


