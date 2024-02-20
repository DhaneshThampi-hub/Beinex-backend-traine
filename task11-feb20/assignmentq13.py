'''13) Write a Python program to check if a string contains only digits.("12345" -->True)'''


def digits(s):
    return s.isdigit()
string = input("enter a string: ")
result = digits(string)
if result:
    print(f"The string '{string}' contains only digits.")
else:
    print(f"The string '{string}' does not contain only digits.")
