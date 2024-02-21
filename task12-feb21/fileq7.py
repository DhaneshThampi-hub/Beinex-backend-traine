'''•	Write a Python program to assess if a file is closed or not'''

file_name = 'file.txt'  

with open(file_name, 'r') as file:
    if not file.closed:
        print(f"The file '{file_name}' is open.")
    else:
        print(f"The file '{file_name}' is closed.")

