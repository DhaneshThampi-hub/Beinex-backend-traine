'''3.	Write a Python code to remove all characters except a           
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e)
'''
string = input("enter a string: ")
character_to_keep = input("enter character to keep: ")
result = ''
for char in string:
    if char == character_to_keep:
        result += char
print(result)