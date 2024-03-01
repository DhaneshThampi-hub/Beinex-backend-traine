"""4. Merge Multiple Text Files into One"""

# Specify the paths of the text files to be merged
file_paths = ["file.txt", "file2.txt", "file3.txt"]

# Specify the path of the output merged file
output_file_path = "merged_file.txt"

# Open the output file in write mode
with open(output_file_path, "w") as output_file:
    # Iterate through each input file
    for file_path in file_paths:
        # Open each input file in read mode
        with open(file_path, "r") as input_file:
            # Read the content of the input file
            file_contents = input_file.read()

            # Write the content to the output file
            output_file.write(file_contents)

            # Optionally, add a newline between the contents of different files
            output_file.write("\n")

print(f"Files merged successfully. Merged content saved to '{output_file_path}'.")
