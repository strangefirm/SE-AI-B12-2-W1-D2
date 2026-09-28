# GETTING FAMILIAR WITH DATATYPES
print("*******************************")
print("String example")
print("*******************************")
course = "GEN AI ARCHITECT"
print("Course Name :", course)
print("length of the course name:", len(course))
print("lower case:", course.lower())
print("first letter:", course[0])
print("last letter:", course[-1])
print("type of course:", type(course))
print("*******************************")
print("Numbers example")
print("*******************************")
#numbers - int and float example
age = 25
height = 5.9
print("Age:", age)
print("Height:", height)
print("Type of age:", type(age))
print("Type of height:", type(height))
print("*******************************")
#tuple example immutable collection
print("Tuple example")
print("*******************************")
tuple_example = (1, 2, 3, 4, 5)
print("Tuple Example:", tuple_example)
print("Type of tuple:", type(tuple_example))

# Access elements
print(tuple_example[0])      # 1
print(tuple_example[-1])     # 5

# Slicing
print(tuple_example[1:4])    # (2, 3, 4)

# Length
print(len(tuple_example))    # 5

# Count occurrences
print(tuple_example.count(2))  # 1

# Find index
print(tuple_example.index(3))  # 2

# Check membership
print(2 in tuple_example)      # True

# Concatenation
more_numbers = tuple_example + (5, 6)
print(more_numbers)

# Repetition
print((1, 2) * 3)         # (1, 2, 1, 2, 1, 2)

# Loop through a tuple
for a in tuple_example:
    print(a * ".")

# Convert list to tuple
values = tuple([1, 2, 3])
print(values)
print("Type of values:", type(values))
print("*******************************")
print("List example")

print("*******************************")
fruits = ["apple", "banana", "mango"]

fruits.append("orange")       # Add an item
fruits.remove("banana")       # Remove an item
print("first element:", fruits[0])              # Access by index
print("Number of items:", len(fruits))            # Number of items
print("Fruits:", fruits)
print("Type of fruits:", type(fruits))
print("*******************************")
print("Set example")
#no duplicates, unordered collection
print("*******************************")
numbers = {1, 2, 3}

numbers.add(4)                # Add an item
numbers.remove(2)             # Remove an item
print(3 in numbers)           # Check membership
print(len(numbers))           # Number of items
numbers.add(1)
print("Numbers:", numbers)
print("Type of numbers:", type(numbers))
print("*******************************")
print("Dictionary example")
print("*******************************")

student = {
    "name": "Ali",
    "age": 20
}

student["course"] = "Python"  # Add a key-value pair
student["age"] = 21           # Change a value
student.pop("course")         # Remove a key-value pair

print(student["name"])        # Access a value
print(student.keys())         # Display keys
print(student.values())       # Display values

print(student)
print("*******************************")
