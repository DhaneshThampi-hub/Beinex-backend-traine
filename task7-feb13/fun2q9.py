'''9.	Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:5
'''


original_list = ['Python', 3, 2, 4, 5, 'version']
max_value = max(filter(lambda x: isinstance(x, (int, float)), original_list))
print("Original list:", original_list)
print("Maximum values in the list using lambda:", max_value)