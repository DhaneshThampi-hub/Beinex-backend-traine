'''6.	Write a Python function that takes a number as a parameter and checks whether the number is prime or not. '''

def prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
result = prime(number)
if result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")