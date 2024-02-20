'''12) Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6]'''


def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
user_input = input("Enter a nested list (e.g., 1, [2, 3], [4, [5, 6]]): ")
try:
    user_list = eval(user_input)  
    flattened_result = flatten_list(user_list)
    print("Original nested list:", user_list)
    print("Flattened list:", flattened_result)
except Exception as e:
    print(f"Error: {e}. Please enter a valid nested list.")
