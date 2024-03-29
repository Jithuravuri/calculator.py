# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2

# Function to calculate power
def power(num1, num2):
    return num1 ** num2

# Function to calculate factorial
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers!"
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Power\n" \
        "6. Factorial\n")

# Take input from the user
select = int(input("Select operations from 1 to 6: "))

if select in range(1, 7):
    number_1 = float(input("Enter first number: "))
    number_2 = None
    if select != 6:
        number_2 = float(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif select == 2:
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif select == 3:
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif select == 4:
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    elif select == 5:
        print(number_1, "**", number_2, "=", power(number_1, number_2))
    elif select == 6:
        print("Factorial of", number_1, "=", factorial(int(number_1)))
else:
    print("Invalid input")