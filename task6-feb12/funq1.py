'''1.	Write a Python function that calculates the factorial of a given integer. 
Demonstrate how to call this function with an example.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
a=int(input("enter a num: "))
result = factorial(a)
print(f"Factorial of {a} :", result)