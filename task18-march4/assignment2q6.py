"""6. Write a Python function that takes a list of strings as input and returns a 
new list with the strings sorted in descending order of their lengths. """


def sort_strings_by_length(input_list):
    """
    Sorts a list of strings in descending order of their lengths.

    Parameters:
    - input_list (list): A list of strings.

    Returns:
    - list: A new list with strings sorted in descending order of their lengths.
    """
    return sorted(input_list, key=len, reverse=True)


# Example usage:
input_strings = input("enter a string by spaces : ").split()
sorted_strings = sort_strings_by_length(input_strings)
print(sorted_strings)
