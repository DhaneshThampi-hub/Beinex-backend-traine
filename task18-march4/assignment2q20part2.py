# main_program
from assignment2q20part1 import get_valid_input

# Example usage of the input_handler library

def main():
    # Get a valid integer input with custom prompt and error message
    age = get_valid_input("Enter your age: ", int, "Age must be a valid integer.", lambda x: x >= 0)

    # Get a valid floating-point input with custom prompt and error message
    height = get_valid_input("Enter your height (in meters): ", float, "Height must be a valid number.", lambda x: x > 0)

    # Get a valid string input with custom prompt
    name = get_valid_input("Enter your name: ", str)

    # Display the entered values
    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} meters")

if __name__ == "__main__":
    main()
