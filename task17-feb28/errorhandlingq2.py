"""Create a program that opens a file and reads its contents.
 Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist.
"""

file_path = input("Enter the path to the file: ")
try:
    with open(file_path, "r") as file:
        contents = file.read()  # to read file contents
        print("File contents:")
        print(contents)  # to print contents in file
except FileNotFoundError:  # exception
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
