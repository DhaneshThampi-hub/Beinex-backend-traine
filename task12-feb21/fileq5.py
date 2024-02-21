'''•	Write a Python program to copy the contents of a file to another file.'''


with open('file.txt', 'r') as firstfile, open('file2.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
