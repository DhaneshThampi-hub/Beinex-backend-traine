"""10.Write a Python function that takes a list of numbers as input and returns 
the sum of all the numbers divisible by 3 or 5."""


def sum_divisible_by_3_or_5(input_list):
    """
    Calculates the sum of numbers divisible by 3 or 5 in a list.

    Parameters:
    - input_list (list): A list of numbers.

    Returns:
    - int: The sum of numbers divisible by 3 or 5.
    """
    return sum(num for num in input_list if num % 3 == 0 or num % 5 == 0)


# Example usage:
lst = input("enter a list  by using space: ").split()
list = [int(num) for num in lst]
result_sum = sum_divisible_by_3_or_5(list)
print(result_sum)
