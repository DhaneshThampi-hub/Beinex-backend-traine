"""2. Count the Number of Lines, Words, and Characters in a Text File"""

# Specify the file path
file_path = "file.txt"

# Initialize counters
line_count = 0
word_count = 0
char_count = 0

# Open the file in read mode
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Count lines
        line_count += 1

        # Count words in each line
        words = line.split()
        word_count += len(words)

        # Count characters in each line
        char_count += len(line)

# Print the results
print(f"Number of lines: {line_count}")
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")
