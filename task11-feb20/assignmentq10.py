'''10) Write a Python program to remove duplicates from a list.'''


def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

lst = input("enter a list  by using space: ").split(' ')
new_list = remove_duplicates(lst)
print(new_list)
