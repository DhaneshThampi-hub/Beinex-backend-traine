'''9) Write a Python program to count the occurrences of an element in a list'''

def count(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

list = input("enter a list by using space: ").split(' ')
element = (input("enter element to count: "))
print(f"{element} has occurred {count(list, element)} times")
