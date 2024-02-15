'''2.Write a Python program to remove duplicates from a list'''

list = [1, 2, 2, 3, 4, 4, 5]
list = []
for item in list:
    if item not in list:
        list.append(item)

print("Original List:", list)
print("List with Duplicates Removed:", list)
