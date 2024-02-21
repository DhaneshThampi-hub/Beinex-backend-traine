'''•	Write a Python program to write a list to a file.'''


list = ['item1', 'item2', 'item3', 'item4']
file_path = 'file4.txt'
with open(file_path, 'w') as file:
    file.writelines('\n'.join(list))
print(f"The list has been written to {file_path}.")
