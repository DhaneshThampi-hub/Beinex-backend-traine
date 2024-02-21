'''•	Write a Python program to read first n lines of a file'''



inputFile = input('enter path of file: ')
N = int(input("Enter N value: "))
with open(inputFile, 'r') as f:
    List = f.readlines()

    print(f"The following are the first {N} lines of the text file:")
    for textline in List[:N]:
        print(textline, end='')
f.close()

