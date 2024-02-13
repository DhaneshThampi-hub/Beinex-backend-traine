'''5.	Write a Python program to check whether a given string is a number or not using Lambda.'''

is_number = lambda s: s.isdigit()
input = input("Enter a string: ")
if is_number(input):
    print(f"The string '{input}' is a number.")
else:
    print(f"The string '{input}' is not a number.")