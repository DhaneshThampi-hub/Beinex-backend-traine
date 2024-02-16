'''5.	Write a Python program to multiply all the items in a dictionary.'''

a=input("enter key1: ")
b=input("enter key2: ")
c=input("enter key3: ")
d=float(input("enter a value for key1: "))
e=float(input("enter a value for key2: "))
f=float(input("enter a value for key3: "))
dict = {a: d, b: e, c: f}
result=1
for value in dict.values():
    result*=value
print(result)