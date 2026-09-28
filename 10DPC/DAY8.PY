def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation: ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Please choose a number from 1 to 5.")
        continue

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = add(first_number, second_number)
    elif choice == "2":
        result = subtract(first_number, second_number)
    elif choice == "3":
        result = multiply(first_number, second_number)
    else:
        result = divide(first_number, second_number)

    print("Result:", result)