print("*******************************")
print("Students Grading System Assignment") 
print("*******************************")

while True:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
    elif marks >= 90:
        grade = "A"
        print("Your grade is:", grade)
    elif marks >= 80:
        grade = "B"
        print("Your grade is:", grade)
    elif marks >= 70:
        grade = "C"
        print("Your grade is:", grade)
    elif marks >= 60:
        grade = "D"
        print("Your grade is:", grade)
    else:
        grade = "F"
        print("Your grade is:", grade)

    print("********************")
    choice = input("Would you like to enter another student's marks? (yes/no): ").strip().lower()
    if choice in ("no", "n"):
        break