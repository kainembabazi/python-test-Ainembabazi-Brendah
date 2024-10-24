# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

marks = int(input("Enter the marks"))
if marks >=90 and marks<=90:
    print("Grade is A")
elif marks >=80 and marks <=80:
    print("Grade is B")
elif marks >=70 and marks <=70:
    print("Grade is C ") 
elif marks >=60 and marks <=60:
    print("Grade is D")
elif marks >=40 and marks <=40:
    print("Grade is F")
else: 
    print("Fail")