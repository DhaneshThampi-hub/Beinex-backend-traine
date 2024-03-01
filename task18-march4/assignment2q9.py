"""9. Write a Python function that takes a list of integers as input and returns a 
new list with only the numbers that are perfect squares"""


def is_perfect_square(num):
    """
    Checks if a given number is a perfect square.

    Parameters:
    - num (int): The number to check.

    Returns:
    - bool: True if the number is a perfect square, False otherwise.
    """
    return num > 0 and int(num**0.5) ** 2 == num


def filter_perfect_squares(input_list):
    """
    Filters perfect square numbers from a list of integers.

    Parameters:
    - input_list (list): A list of integers.

    Returns:
    - list: A new list with only the perfect square numbers.
    """
    return [num for num in input_list if is_perfect_square(num)]


# Example usage:
lst = input("enter a list  by using space: ").split()
list = [int(num) for num in lst]
perfect_squares = filter_perfect_squares(list)
print(perfect_squares)
