"""Write a program that opens a file, reads its contents, and writes the contents to a new file. Use a try-except-finally block
 to ensure that the file is closed even if an exception occurs during the file operations.
"""


def copy_file_content(input_file_path, output_file_path):
    try:
        # Open the input file in read mode
        with open(input_file_path, "r") as input_file:
            # Read the contents of the input file
            file_contents = input_file.read()

        # Open the output file in write mode
        with open(output_file_path, "w") as output_file:
            # Write the contents to the output file
            output_file.write(file_contents)

    except Exception as e:
        # Handle exceptions, if any
        print(f"An error occurred: {e}")

    finally:
        # Ensure that the input file is closed, even if an exception occurs
        if "input_file" in locals() and not input_file.closed:
            input_file.close()

        # Ensure that the output file is closed, even if an exception occurs
        if "output_file" in locals() and not output_file.closed:
            output_file.close()


# Example usage:
input_file_path = "file.txt"
output_file_path = "output.txt"

copy_file_content(input_file_path, output_file_path)
