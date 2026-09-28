print("*******************************")
print("IF, NESTED IF AND TERNARY OPERATOR") 
print("*******************************")
print("Simple if example")
print("*******************************")
#SIMPLE IF, NESTED IF AND TERNARY OPERATOR
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
elif marks >= 60 and marks < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

print("*******************************")
print("Nested if example")
print("*******************************")

age = int(input("Enter your age: "))

if age >= 18:
    print("Age requirement completed.")
    has_payment_method = input("Do you have a payment method? (y/n):")  
    if( (has_payment_method == "y" or has_payment_method == "Y") ):
        print("You are eligible to subscribe to Netflix.")
    else:
        print("You need a payment method to subscribe.")
else:
    print("You must be 18 or older to subscribe.")
print("*******************************")
print("Ternary operator example")
print("*******************************")
order_amount = float(input("Enter your order amount: "))
    
delivery_message = (
        "Free delivery"
        if order_amount >= 500
        else "Delivery charge: ₹50"
    )
    
print(delivery_message)