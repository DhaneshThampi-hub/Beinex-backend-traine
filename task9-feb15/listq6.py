'''6.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]'''

list = [2, 4, 6, 8, 10, 12, 14]
square_greater_than_50 = [x ** 2 for x in list if x ** 2 > 50]
print(square_greater_than_50)
