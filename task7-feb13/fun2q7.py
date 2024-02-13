'''7.	Write a Python program to find palindromes in a given list of strings using Lambda.'''


is_palindrome = lambda s: s == s[::-1]
word_list = ["level", "python", "radar", "hello", "deed"]
palindromes = [word for word in word_list if is_palindrome(word)]
print("Palindromes in the list:", palindromes)