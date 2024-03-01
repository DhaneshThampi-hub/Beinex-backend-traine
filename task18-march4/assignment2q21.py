"""21.Write a Python program that executes an operation on a list and handles an 
IndexError exception if the index is out of range"""


def perform_operation_on_list(my_list, index):
    try:
        result = (
            my_list[index] ** 2
        )  # Example operation: Squaring the element at the specified index
        print(f"Result of the operation: {result}")
    except IndexError:
        print("Error: Index is out of range. Please provide a valid index.")


# Example usage with user-friendly features:
my_list = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter the index to perform the operation: "))
        perform_operation_on_list(my_list, index)
        break  # Break out of the loop if the operation is successful
    except ValueError:
        print("Error: Please enter a valid integer for the index.")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
