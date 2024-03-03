# Import the necessary functions from the assignment2q20part1 module
import assignment2q20part1

def main():
    # Example using the input_handler library
    # Get a non-empty string input for the user's name
    name = assignment2q20part1.get_non_empty_string("Enter your name: ")

    # Get an integer input for the user's age
    age = assignment2q20part1.get_integer_input("Enter your age: ")

    # Get a floating-point input for the user's height in meters
    height = assignment2q20part1.get_float_input("Enter your height in meters: ")

    # Display the collected information
    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} meters")

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
