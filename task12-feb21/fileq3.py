'''•	Write a Python program to append text to a file and display the text.'''



file_name =  input('enter path of file: ')
text_to_append = input("enter text to append: ") 

with open('file.txt', 'a') as file:
    file.write(text_to_append + '\n')  
with open(file_name, 'r') as file:
    print("Updated content of the file:")
    print(file.read())

