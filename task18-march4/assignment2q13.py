"""13.Implement a program that simulates a basic calculator, allowing users to 
perform arithmetic operations (addition, subtraction, multiplication, 
division) on two numbers. """


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


print("The operations are: ")
print("1.Add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.exit")
try:
    num1 = float(input("enter a num1: "))
    num2 = float(input("enter a num2: "))
    while 1:
        choice = input("enter u r choice: ")
        if choice == "5":
            print("enter a valid choice!! or exit")
            break
        if choice == "1":
            print(addition(num1, num2))
        elif choice == "2":
            print(subtraction(num1, num2))
        elif choice == "3":
            print(multiplication(num1, num2))
        elif choice == "4":
            print(division(num1, num2))
except ValueError:
    print("Error: Please enter valid numeric values for numbers.")
except Exception as e:
    print(f"Error: {e}")
