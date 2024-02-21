'''•	Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'''


file_name=input("enter a file name: ")
alphabets='abcdefghijklmnopqrstuvwxyz'
with open(file_name,'w')as file:
    lettr=int(input('enter number of letters per line: '))
    for i in range(0,len(alphabets),lettr):
        line=alphabets[i:i+lettr]
        file.write(line+'\n')
    print(f"alphabet file'{file_name}'created sucessfully")