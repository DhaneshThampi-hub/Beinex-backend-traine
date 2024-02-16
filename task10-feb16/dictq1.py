'''1.	Write a Python program to merge two Python dictionaries.'''

def merge_dicts(dict1, dict2, merge='1'):
    if merge== '1':
        merged_dict = {**dict1, **dict2}
    elif merge == '2':
        merged_dict = {**dict2, **dict1}
    else:
        raise ValueError("Invalid merge strategy. Choose 'first' or 'second'.")
    return merged_dict
a=input("enter a key1 for dict1: ")
b=input("enter a key2 for dict1: ")
c=input("enter a value for dict1: ")
d=input("enter a value for dict1: ")
e=input("enter a key1 for dict2: ")
f=input("enter a key2 for dict2: ")
g=input("enter a value for key2: ")
h=input("enter a value for key2: ")
dict1 = {a: c, b: d}
dict2 = {e: g, f: h}
merge_strategy = input("Enter merge strategy ('first' or 'second'): ")
result = merge_dicts(dict1, dict2, merge_strategy)
print("Merged Dictionary:", result)

