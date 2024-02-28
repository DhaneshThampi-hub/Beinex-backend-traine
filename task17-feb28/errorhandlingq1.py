"""1.Write a Python program that prompts the user to enter an integer and handles the ValueError exception 
if the user enters a non-integer value.
"""

while True:
    try:
        user_input = input("Please enter an integer: ")
        user_integer = int(user_input)
        print("You entered:", user_integer)
        break  # Exit the loop if conversion to integer is successful
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
