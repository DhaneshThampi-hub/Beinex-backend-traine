"""16.Count the total number of uppercase characters in a file in Python
"""


def count_uppercase_characters(file_path):
    try:
        with open(file_path, "r") as file:
            # Read the entire content of the file
            file_contents = file.read()

            # Count the uppercase characters
            uppercase_count = sum(1 for char in file_contents if char.isupper())

        print(f"Total Uppercase Characters in '{file_path}': {uppercase_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
file_path = "file.txt"
count_uppercase_characters(file_path)
