'''6.	Write a Python program to get the maximum and minimum values of a dictionary'''


while 1:
    a=input("enter key1: ")
    b=input("enter key2: ")
    c=input("enter key3: ")
    d=float(input("enter a value for key1: "))
    e=float(input("enter a value for key2: "))
    f=float(input("enter a value for key3: "))
    my_dict = {a: d, b: e, c: f}
    max_value = max(my_dict.values())
    min_value = min(my_dict.values())
    print(f"Maximum Value: {max_value}")
    print(f"Minimum Value: {min_value}")
