'''4.Write a Python program to print the numbers of a specified list after removing even numbers from it
	list = [24,34,53,65,78,93,23,42]'''

list = [24, 34, 53, 65, 78, 93, 23, 42]
for num in list:
    if num % 2 != 0:
        print(num,end=" ")