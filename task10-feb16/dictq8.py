'''8.	Create a function that takes a string and returns a dictionary where keys are 
letters, and values are the number of times each letter appears in the string '''

def count_letters(input_string):
    letter_counts = {}  
    for char in input_string:
        if char.isalpha():  
            char_lower = char.lower()  
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
    return letter_counts
string = input('enter a string: ')
result = count_letters(string)
print(result)
