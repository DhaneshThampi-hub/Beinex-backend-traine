'''4.	Write a Python program to sum all the items in a dictionary.'''

while 1:
    a=input("enter key1: ")
    b=input("enter key2: ")
    c=input("enter key3: ")
    d=float(input("enter a value for key1: "))
    e=float(input("enter a value for key2: "))
    f=float(input("enter a value for key3: "))
    my_dict = {a: d, b: e, c: f}
    result = sum(value for value in my_dict.values())
    print(result)
