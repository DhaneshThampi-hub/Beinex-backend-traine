'''11) Write a Python program to find the intersection of two lists'''


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = input("enter a list1  by using space").split(' ')
lst2 = input("enter a list2  by using space").split(' ')
print(intersection(lst1, lst2)) 
