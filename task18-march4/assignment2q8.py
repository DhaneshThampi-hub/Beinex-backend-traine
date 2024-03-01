"""8. Write a Python program that takes a list of integers as input and returns a 
new list with only the numbers that are prime. """


def is_prime(num):
    """
    Checks if a given number is prime.

    Parameters:
    - num (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_primes(input_list):
    """
    Filters prime numbers from a list of integers.

    Parameters:
    - input_list (list): A list of integers.

    Returns:
    - list: A new list with only the prime numbers.
    """
    return [num for num in input_list if is_prime(num)]


# Example usage:
lst = input("enter a list  by using space: ").split()
list = [int(num) for num in lst]
prime_numbers = filter_primes(list)
print(prime_numbers)
