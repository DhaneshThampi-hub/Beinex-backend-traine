'''2.	Write a Python program to create a function that takes one 
argument, and that argument will be multiplied with an unknown given number.'''

def multiply(x):
    unknown_number = 20
    result = x * unknown_number
    return result
input = float(input("Enter a number to be multiplied: "))
result = multiply(input)
print("Result after multiplying with unknown number:", result)