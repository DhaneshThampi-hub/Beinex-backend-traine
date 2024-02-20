'''19) Write a Python program to count the number of vowels in a string.'''

def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
string = input("enter a string: ")
print(f"The number of vowels in '{string}' is: {count_vowels(string)}")
