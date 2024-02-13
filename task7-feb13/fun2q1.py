'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also 
create a lambda function that multiplies argument x with argument y and prints the result.'''

add = lambda x: x + 15
mul = lambda x, y: x * y
number = int(input("Enter a number: "))
result = add(number)
print("Result after adding 15:", result)

num1 = float(input("Enter the first number for multiplication: "))
num2 = float(input("Enter the second number for multiplication: "))
result_mul = mul(num1, num2)
print("Result of multiplication:", result_mul)