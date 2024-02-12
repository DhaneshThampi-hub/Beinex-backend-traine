'''7.	Write a Python program that accepts a hyphen-separated sequence of words as input and prints
 the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

input_sequence = input("Enter hyphen-separated sequence of words: ")
result_sequence = '-'.join(sorted(input_sequence.split('-')))
print("Sorted Result:", result_sequence)