'''7.	Write a Python program that accepts a hyphen-separated sequence of words as input and prints
 the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

def sort_sequence(sequence): 
    result_sequence = '-'.join(sorted(input_sequence.split('-')))
    return result_sequence
input_sequence = input("Enter hyphen-separated sequence of words: ")
print(sort_sequence(input_sequence))
