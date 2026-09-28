#STRING OPERATIONS AND ARITHMETIC OPERATIONS
print("HELLO")
a = 10
b = 3
print("********************************")
print("Arithmetic operations")
print("*******************************")
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Remainder: 1
print(a ** b)  # Power: 1000

print(a > b)   # True
print(a == b)  # Falsea += 2   # a = a + 2
a -= 1   # a = a - 1
a *= 3   # a = a * 3

print(a)
print("**************************")
print("Operations using string")
print("***************************")
text = "FATHIMA SUHAILA"

# Access characters
print(text[0])        # F
print(text[-1])       # A

# Length
print(len(text))      # 12

# Convert case
print(text.upper())   # FATHIMA SUHAILA
print(text.lower())   # fathima suhaila

# Replace text
print(text.replace("FATHIMA", "MARYAM"))  # MARYAM SUHAILA

# Split string
words = text.split()
print(words)          # ['FATHIMA', 'SUHAILA']

# Join strings
print("-".join(words))  # FATHIMA-SUHAILA

# Check content
print("FATHIMA" in text)  # True
print(text.startswith("FATHIMA"))  # True

# Remove extra spaces
name = "  Ali  "
print(name.strip())    # Ali

# Concatenate strings
first = "Hello"
second = "World"
print(first + " " + second)
