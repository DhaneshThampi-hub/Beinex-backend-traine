"""20.Create a Python library with the function to input the values with 
expectation handling and demonstrate with the example"""





def get_integer_input(prompt):
    """
    Get a valid integer input from the user.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    - int: Valid user input as an integer.
    """
    while True:
        try:
            # Attempt to convert user input to an integer
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            # Handle invalid input by displaying an error message
            print("Invalid input! Please enter a valid integer.")

def get_float_input(prompt):
    """
    Get a valid floating-point input from the user.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    - float: Valid user input as a floating-point number.
    """
    while True:
        try:
            # Attempt to convert user input to a float
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            # Handle invalid input by displaying an error message
            print("Invalid input! Please enter a valid floating-point number.")

def get_non_empty_string(prompt):
    """
    Get a non-empty string input from the user.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    - str: Valid user input as a non-empty string.
    """
    while True:
        # Get user input and remove leading/trailing whitespaces
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            # Handle empty input by displaying an error message
            print("Input cannot be empty. Please try again.")






