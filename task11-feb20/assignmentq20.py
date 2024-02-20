'''20) Write a Python program to remove all occurrences of a given element from a list'''


def remove_items(test_list, item):
    return [i for i in test_list if i != item]
original_list = input("enter a list by using space: ").split()
remove = input("enter item to remove: ")
updated_list = remove_items(original_list, remove)
print(f"The list after removing all occurrences of {remove} is: {updated_list}")
