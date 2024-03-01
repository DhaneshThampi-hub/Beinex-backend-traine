"""Write a Python function called calculate_discounted_price that takes the 
original price of an item and a discount percentage as input. The function 
should return the discounted price after applying the discount. Ensure that 
the function handles the case where the discount percentage is negative 
and raises a custom exception called InvalidDiscountError with an 
appropriate error message"""


class InvalidDiscountError(Exception):
    """Custom exception for invalid discount percentage."""

    pass


def calculate_discounted_price():
    """
    Calculate the discounted price after applying the discount.

    Returns:
    - float: The discounted price.

    Raises:
    - InvalidDiscountError: If the discount percentage is negative.
    """
    try:
        # Get user input for original price
        original_price = float(input("Enter the original price of the item: $"))

        # Get user input for discount percentage
        discount_percentage = float(input("Enter the discount percentage: "))

        if discount_percentage < 0:
            raise InvalidDiscountError("Error: Discount percentage cannot be negative")

        # Calculate discounted price
        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount

        return discounted_price

    except ValueError:
        print(
            "Error: Please enter valid numeric values for original price and discount percentage."
        )
        return None
    except InvalidDiscountError as e:
        print(f"Error: {e}")
        return None


# Example usage:
discounted_price = calculate_discounted_price()
if discounted_price is not None:
    print(f"Discounted Price: ${discounted_price}")
