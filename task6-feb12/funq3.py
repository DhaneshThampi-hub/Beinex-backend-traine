'''3.	Write a Python function to find the maximum of three numbers.'''

def find_max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
result = find_max_of_three(num1, num2, num3)
print("The maximum of the three numbers is:", result)