# Que5)The marks obtained by a student in 3 different subjects are input by the user. Your program should 
#   calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
#   Average Grade
#   90-100 A
#   80-89 B
#   70-79 C
#   60-69 D
#   0-59 F

sub1 = int(input("Enter the marks of 1st subject: "))
sub2 = int(input("Enter the marks of 2nd subject: "))
sub3 = int(input("Enter the marks of 3rd subject: "))
print("---------------------------------------------")

avg = (sub1 + sub2 + sub3)/3

if (avg >= 90) and (avg < 100):
    print("A grade")
elif (avg >= 80) and (avg < 89):
    print("B grade")
elif (avg >= 70) and (avg < 79):
    print("C grade")
elif (avg >= 60) and (avg < 69):
    print("D grade")
else:
    print("Fail")