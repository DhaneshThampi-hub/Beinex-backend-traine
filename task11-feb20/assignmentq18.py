'''18) Write a Python program to find the second largest number in a list'''

def second_largest(lst):
    new_list = set(lst)
    new_list.remove(max(new_list))
    return max(new_list)

list = input("enter a list  by using space: ").split()
list=[int(num)for num in list]
print(f"The second largest number is: {second_largest(list)}")