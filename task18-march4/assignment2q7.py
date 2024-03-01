"""7. Write a function that takes a list of numbers as input and returns the 
second-largest number. 
"""


def second_largest(lst):
    if len(lst) < 2:
        return "List should have at least two numbers."

    new_list = set(lst)
    new_list.remove(max(new_list))
    return max(new_list)

try:
    # Get user input
    user_input = input("Enter a list of numbers separated by space: ")
    
    # Convert input to a list of integers
    user_list = [int(num) for num in user_input.split()]

    # Call the function and display the result
    result = second_largest(user_list)
    print(f"The second-largest number is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid list of numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
