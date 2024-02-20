'''7) Write a Python program to implement a binary search on a sorted list.
'''
 
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low <= high:
       mid = (low + high) // 2
       if arr[mid] == target:
           return mid
       elif arr[mid]<target:
           low=mid+1
       else:
           high= mid - 1 
    return -1
sorted_list= input("Enter a sorted list of numbers (comma-separated): ")
sorted_list = [int(num) for num in sorted_list.split(',')]
target = int(input("Enter the target value to search: "))
result = binary_search(sorted_list, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")