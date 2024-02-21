'''•	Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space
'''


file_name = 'file2.txt' 
with open(file_name, 'r') as file:
    data = file.read()
    words = data.split() 
    for word in words:
        word = word.rstrip(',')
        if word:  
            print(word)
        print(f"Total number of words: {len(words)}")
