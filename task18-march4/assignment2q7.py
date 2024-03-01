"""7. Write a function that takes a list of numbers as input and returns the 
second-largest number. 
"""


def second_largest(lst):
    new_list = set(lst)
    new_list.remove(max(new_list))
    return max(new_list)


list = input("enter a list  by using space: ").split()
list = [int(num) for num in list]
print(f"The second largest number is: {second_largest(list)}")
