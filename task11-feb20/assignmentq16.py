'''16) Write a Python program to merge two sorted lists into a single sorted list'''


from assignmentq10 import remove_duplicates
def sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

list1 = input("enter a list1  by using space: ").split(' ')
list2 = input("enter a list2  by using space: ").split(' ')
sorted_list = sorted_lists(list1, list2)
print("The combined sorted list is:",remove_duplicates( sorted_list))

