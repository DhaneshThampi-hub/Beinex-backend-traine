"""1. Read and Print the Contents of a Text File"""

# Specify the file path
file_path = "file.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.read()

    # Print the contents
    print(file_contents)
