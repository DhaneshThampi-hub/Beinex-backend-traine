'''6.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]'''

list = [2, 4, 6, 8, 10, 12, 14]
new_list = []
for num in list:
    if num**2 > 50:
        new_list.append(num**2)
print(new_list)