# ==========================================================
# Basic Python Calculator
# Author: Your Name
# Description:
# A simple calculator that performs basic arithmetic
# operations using Python fundamentals.
# ==========================================================


# -------------------------------
# Function for Addition
# -------------------------------
def add(a, b):
    # Returns the sum of two numbers
    return a + b


# -------------------------------
# Function for Subtraction
# -------------------------------
def subtract(a, b):
    # Returns the difference of two numbers
    return a - b


# -------------------------------
# Function for Multiplication
# -------------------------------
def multiply(a, b):
    # Returns the product of two numbers
    return a * b


# -------------------------------
# Function for Division
# -------------------------------
def divide(a, b):
    # Division by zero is not allowed
    if b == 0:
        return "Error! Division by zero is not possible."

    return a / b


# ==========================================================
# Main Program
# ==========================================================

print("=" * 40)
print("      WELCOME TO PYTHON CALCULATOR")
print("=" * 40)

# Infinite loop so the calculator keeps running
while True:

    # Display menu
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Take user choice
    choice = input("\nEnter your choice (1-5): ")

    # Exit condition
    if choice == "5":
        print("\nThank you for using the calculator!")
        break

    # Validate menu choice
    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please try again.")
        continue

    # Error handling for invalid number input
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

    except ValueError:
        print("\nPlease enter valid numeric values.")
        continue

    # Perform selected operation
    if choice == "1":
        result = add(first_number, second_number)
        print(f"\nResult = {result}")

    elif choice == "2":
        result = subtract(first_number, second_number)
        print(f"\nResult = {result}")

    elif choice == "3":
        result = multiply(first_number, second_number)
        print(f"\nResult = {result}")

    elif choice == "4":
        result = divide(first_number, second_number)
        print(f"\nResult = {result}")
