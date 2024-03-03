"""13.Implement a program that simulates a basic calculator, allowing users to 
perform arithmetic operations (addition, subtraction, multiplication, 
division) on two numbers. """


def addition(a, b):
    return a + b  # returns the sum


def subtraction(a, b):
    return a - b  # returns the difference


def multiplication(a, b):
    return a * b  # returns the product


def division(a, b):
    if b != 0:
        return a / b  # returns the quotient
    else:
        return "Cannot divide by zero"


# Main program
print("The operations are: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    while True:
        choice = input("Enter your choice (1-5): ")  # User choice input
        if choice == "5":
            print("Exiting the program.")
            break

        if choice == "1":
            print(addition(num1, num2))
        elif choice == "2":
            print(subtraction(num1, num2))
        elif choice == "3":
            print(multiplication(num1, num2))
        elif choice == "4":
            print(division(num1, num2))
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

except ValueError:
    print("Error: Please enter valid numeric values for numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

 
