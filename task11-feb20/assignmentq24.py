'''24) Write a Python program to calculate the sum of all elements in a list recursively'''

def sum_recursive(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_recursive(lst[1:])
list = input("enter a list  by using space: ").split()
list=[int(num)for num in list]
total_sum = sum_recursive(list)
print(f"The sum of elements in the list is: {total_sum}")
