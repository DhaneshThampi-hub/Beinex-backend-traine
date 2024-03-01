"""2.Write a Python program input and add two integers only and handle the 
exceptions.
RUN 1:
Enter First Value: 10
Enter Second Value: 20
0.5
RUN 2:
Enter First Value: 10
Enter Second Value: Hello
Pls Input Integer Only invalid literal for int() with base 10: 'Hello'
RUN 3:
Enter First Value: 10
Enter Second Value: 0
Second Number Should Not Be Zero division by zero"""


def add_two_integers():
    while True:
        try:
            first_value = int(input("Enter First Value: "))
            second_value = int(input("Enter Second Value: "))

            if second_value == 0:
                raise ValueError("Second Number Should Not Be Zero")

            result = first_value / second_value
            print(f"Result of the division: {result}")
            break  # Break out of the loop if the operation is successful

        except ValueError as ve:
            print(f"Error: {ve}. Please enter valid integers.")
            ask_retry = input("Do you want to try again? (y/n): ").lower()
            if ask_retry != "y":
                break
        except ZeroDivisionError as zde:
            print(f"Error: {zde}. Please enter a non-zero value for the second number.")
            ask_retry = input("Do you want to try again? (y/n): ").lower()
            if ask_retry != "y":
                break
        except Exception as e:
            print(f"Unexpected error: {e}")
            ask_retry = input("Do you want to try again? (y/n): ").lower()
            if ask_retry != "y":
                break


# Example usage:
add_two_integers()
