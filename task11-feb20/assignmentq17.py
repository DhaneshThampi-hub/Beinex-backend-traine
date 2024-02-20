'''17) Write a Python program to find the sum of all even numbers in a list.'''

def sum_of_even_numbers(lst):
    result = 0
    for item in lst:
        if item % 2 == 0:
            result += item
    return result

list = input("enter a list  by using space: ").split()
list=[int(num)for num in list]
even_sum = sum_of_even_numbers(list)
print(f"The sum of even numbers in the list is: {even_sum}")
