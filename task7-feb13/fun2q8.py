'''8.	Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
'''


multiply = lambda number, lst: [x * number for x in lst]
number = int(input("Enter a number to multiply with: "))
number_list = [2, 4, 6, 9, 11]
result = multiply(number, number_list)
print(f"Result after multiplying each number with {number}:", result)