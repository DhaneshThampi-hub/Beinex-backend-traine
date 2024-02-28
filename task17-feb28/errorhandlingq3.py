"""Write a program that calculates the division of two numbers entered by the user. 
Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message 
if the user tries to divide by zero.
"""

while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator  # division
        print(f"Result of division: {result}")
        break  # Exit the loop if division is successful
    except ValueError:
        print("Invalid input! Please enter valid numerical values.")
    except ZeroDivisionError:
        print(
            "Error: Division by zero is not allowed. Please enter a non-zero denominator."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
