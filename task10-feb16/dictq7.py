
'''7.	Write a Python program to Delete a list of keys from a dictionary'''

while 1:
    a=input("enter key1: ")
    b=input("enter key2: ")
    c=input("enter key3: ")
    d=input("enter a value for key1: ")
    e=input("enter a value for key2: ")
    f=input("enter a value for key3: ")
    g=input('enter a key to remove: ')
    my_dict = {a: d, b: e, c:f}
    del my_dict[g]
    print(my_dict)
