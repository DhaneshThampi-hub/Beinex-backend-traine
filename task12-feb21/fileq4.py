'''•	Write a Python program to read a file line by line store it into a variable.'''

file_name =  input('enter path of file: ')

with open('file.txt', 'r') as file:
    data = file.readlines()  
    print("Contents of the file:")
    for line in data:
        print(line.strip())  
