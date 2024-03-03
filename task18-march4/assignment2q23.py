"""23.The program takes input from the user and checks if whether the input 
value is an integer or not, if the input value is not an integer then the 
program will through a Type exception.
Run 1: 
Enter First Number: 43
43
Run 2:
Enter First Number: 123.1
Invalid Input..Please Input Integer Only..
Enter First Number: 43
43"""


def get_integer_input():
    while True:
        try:
            user_input = input("Enter First Number: ")
            result = int(user_input)
            print(f'{result} is  an integer')
            break  # Break out of the loop if the operation is successful

        except ValueError:
            print(f"Error: Invalid Input,{user_input} is not an integer. Please Input an Integer.")
            ask_retry = input("Do you want to try again? (y/n): ").lower()
            if ask_retry != "y":
                break


# Example usage:
get_integer_input()
