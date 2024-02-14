'''2.	Print even length words in a string.
Sample String : "I love coding"
Expected Result : “love, coding”
'''
string = "I love coding"
words = string.split()
even_length_words = []
for word in words:
    if len(word) % 2 == 0:
        even_length_words.append(word)
result = ', '.join(even_length_words)
print(result)