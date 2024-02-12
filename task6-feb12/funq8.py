'''8.	Define a function that accepts 2 values and return its sum, subtraction and multiplication. 
Using 4 types of functions based on arguments and return type.'''

#1. with argument with return type

def operations(x, y):
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    return sum, subtraction, multiplication
a=float(input('enter a value: '))
b=float(input('enter a value: '))
result = operations(a, b)
print("Result:", result)

#2. with argument without return type

def perform_operations_no_return(a, b):
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
x=float(input('enter a val: '))
y=float(input('enter a val: '))
perform_operations_no_return(x, y)

#3. without argument with return type

def operations1():
    x=float(input('enter a value: '))
    y=float(input('enter a value: '))
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    return sum, subtraction, multiplication
print(operations1())


#4. without argument without return type
def operations2():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
operations2()
