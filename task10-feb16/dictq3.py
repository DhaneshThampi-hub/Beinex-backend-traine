'''3.	Write a Python program to print a dictionary where the keys are numbers
 between 1 and 15 (both included) and the values are the square of the keys'''

while 1:
    a=int(input("enter a  start limit: "))
    b=int(input("enter end limit: "))
    square_dict = {}
    for i in range(a, b+1):
        square_dict[i] = i**2
    print(square_dict)
