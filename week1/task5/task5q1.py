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
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot find modulus with zero"
def exponentiation(a, b):
    return a ** b
def floor_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot perform floor division by zero"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition:", addition(num1, num2))
print("Subtraction:", subtraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))
print("Modulus:", modulus(num1, num2))
print("Exponentiation:", exponentiation(num1, num2))
print("Floor Division:", floor_division(num1, num2))


