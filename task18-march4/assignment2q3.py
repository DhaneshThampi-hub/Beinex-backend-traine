"""3. Search for a String in a Text File"""

# Specify the file path
file_path = "file.txt"
# Specify the string to search for
search_string = "Hello how are you"

# Open the file in read mode
with open(file_path, "r") as file:
    # Initialize a list to store line numbers where the search string is found
    matching_lines = []

    # Iterate through each line in the file
    for line_number, line in enumerate(file, 1):
        # Check if the search string is present in the line
        if search_string in line:
            matching_lines.append(line_number)

    # Print the results
    if matching_lines:
        print(
            f"Found '{search_string}' in the file at line(s): {', '.join(map(str, matching_lines))}"
        )
    else:
        print(f"'{search_string}' not found in the file.")
