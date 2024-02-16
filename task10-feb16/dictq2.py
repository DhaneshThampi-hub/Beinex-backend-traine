'''2.	Write a Python program to get dictionary keys as a list'''

def keys_as_list(dictionary):
    keys_list = []
    value_list=[]
    for key in dictionary.keys():
        keys_list.append(key)
    for value in dictionary.values():
        value_list.append(value)
    return keys_list,value_list

a=input("enter key1: ")
b=input("enter key2: ")
c=input("enter key3: ")
d=input("enter a value for key1: ")
e=input("enter a value for key2: ")
f=input("enter a value for key3: ")
dict = {a: d, b: e, c: f}
print(keys_as_list(dict))  
