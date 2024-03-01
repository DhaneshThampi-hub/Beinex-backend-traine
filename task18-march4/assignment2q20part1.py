"""20.Create a Python library with the function to input the values with 
expectation handling and demonstrate with the example"""



def get_valid_input(prompt, expected_type, error_message="Invalid input. Please try again.", custom_validation=None):
    """
    Get valid user input with expectation handling.

    Parameters:
    - prompt (str): The prompt to display to the user.
    - expected_type (type): The expected data type of the input.
    - error_message (str): Custom error message to display on invalid input.
    - custom_validation (function): Custom validation function to check additional conditions.

    Returns:
    - Variable: Valid user input of the expected type.
    """
    while True:
        try:
            user_input = expected_type(input(prompt))
            if custom_validation and not custom_validation(user_input):
                raise ValueError("Custom validation failed.")
            return user_input
        except ValueError:
            print(error_message)
