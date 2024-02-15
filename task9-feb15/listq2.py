'''2.Write a Python program to remove duplicates from a list'''

my_list = [1, 2, 2, 3, 4, 4, 5]
list = []
for item in my_list:
    if item not in list:
        list.append(item)

print("Original List:", my_list)
print("List with Duplicates Removed:", list)