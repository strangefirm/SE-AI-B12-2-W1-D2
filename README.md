[README.md](https://github.com/user-attachments/files/32784425/README.md)
# Student Grading System

A simple, interactive **Student Grading System** developed using Python.
This beginner-friendly console application accepts student marks,
validates the input, assigns grades, and allows the user to process
multiple students in one session.

> **Project type:** Python Console Application\
> **Repository:**
> [SE-AI-B12-2-W1-D2](https://github.com/strangefirm/SE-AI-B12-2-W1-D2)

------------------------------------------------------------------------

## Project Overview

The Student Grading System automates the basic task of converting
students' marks into grades. Instead of calculating grades manually, the
user enters a student's marks and the program displays the corresponding
grade.

The program also checks whether the entered marks are within the valid
range and gives the user the option to enter marks for another student.

## Features

-   Accepts student marks through the console.
-   Validates marks to ensure they are between **0 and 100**.
-   Displays an appropriate grade based on the entered marks.
-   Allows multiple students to be processed in one run.
-   Uses a simple, user-friendly command-line interaction.
-   Handles invalid mark entries with an error message.

## Python Concepts Used

This project demonstrates the practical use of fundamental Python
programming concepts:

  -----------------------------------------------------------------------
  Concept                             How it is used
  ----------------------------------- -----------------------------------
  Variables                           Store marks, grade results, and
                                      user responses.

  Data types                          Use integers or numeric values for
                                      marks and strings for responses and
                                      grades.

  Operators                           Use comparison operators to
                                      validate marks and determine grade
                                      ranges; assignment and logical
                                      operators support program flow
                                      where applicable.

  Conditional statements              `if`, `elif`, and `else` select the
                                      correct grade and handle invalid
                                      marks.

  Loops                               Repetition allows the program to
                                      accept marks for multiple students.

  Functions                           Functions can organize reusable
                                      tasks such as validating marks or
                                      assigning grades, if implemented in
                                      the source code.

  User input and output               `input()` receives user entries and
                                      `print()` displays instructions and
                                      results.
  -----------------------------------------------------------------------

> **Note:** The concepts above describe the project's learning scope.
> Update the functions row or any other item to match the exact
> implementation in your Python source file.

## Sample Execution

``` text
********************************
Students Grading System Assignment
********************************
Enter your marks: 105
Invalid marks. Please enter marks between 0 and 100.

Would you like to enter another student's marks? (yes/no): y
Enter your marks: 90
Your grade is: A

Would you like to enter another student's marks? (yes/no): y
Enter your marks: 40
Your grade is: F

Would you like to enter another student's marks? (yes/no): y
Enter your marks: 100
Your grade is: A

Would you like to enter another student's marks? (yes/no): n
```

*The sample output is based on the demonstration shown for this project.
Grade boundaries should be checked against the rules in the actual
source code.*

## Requirements

-   Python 3.x
-   A terminal or command prompt

No external Python packages are required for a basic console
implementation.

## How to Run

1.  **Clone the repository:**

    ``` bash
    git clone https://github.com/strangefirm/SE-AI-B12-2-W1-D2.git
    ```

2.  **Open the project folder:**

    ``` bash
    cd SE-AI-B12-2-W1-D2
    ```

3.  **Run the Python file:**

    Locate the project's main `.py` file and run it with Python:

    ``` bash
    python filename.py
    ```

    Replace `filename.py` with the actual name of the Python file. On
    some systems, use `python3 filename.py`.

## Learning Outcomes

By completing this project, learners can practice:

-   Writing and running a Python program.
-   Working with basic data types and variables.
-   Applying operators and conditional logic.
-   Using loops for repeated user interaction.
-   Validating user input.
-   Organizing code into functions when applicable.
-   Building a small, practical command-line application.

## Possible Improvements

Future versions could include:

-   Student names or student ID input.
-   A summary of all students and their grades.
-   More detailed input validation for non-numeric values.
-   Saving results to a text file, CSV file, or database.
-   A graphical user interface.

## Author

**Fathima Suhaila**

------------------------------------------------------------------------

*Created as a Python programming assignment to demonstrate foundational
programming concepts through a practical Student Grading System.*
