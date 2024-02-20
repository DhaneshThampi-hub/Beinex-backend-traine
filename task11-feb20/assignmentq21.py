'''21) Write a Python program to remove all whitespace characters from a string.'''


string=input('enter a string: ')
s=''.join(char for char in string if not char.isspace())
print(s)