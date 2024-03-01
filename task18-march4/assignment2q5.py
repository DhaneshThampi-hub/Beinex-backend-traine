"""5. Implement a program that reads a text file and counts the occurrences of 
each word, ignoring case sensitivity. """

# Specify the file path
file_path = "file.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read the entire content of the file
    file_contents = file.read()

    # Convert all words to lowercase and split the text into a list of words
    words = file_contents.lower().split()

    # Initialize a dictionary to count word occurrences
    word_counts = {}

    # Count occurrences of each word
    for word in words:
        # Remove punctuation (if needed)
        word = word.strip(".,!?\"'()[]{}:;")

        # Update the word count in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

    # Print the results
    print("Word Occurrences (ignoring case):")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
