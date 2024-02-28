'''Write a Python program that prompts the user to enter their age. Define a custom exception called InvalidAgeError 
that is raised when the entered age is less than 0 or greater than 150. 
Handle the InvalidAgeError exception and display an appropriate error message.
'''

class InvalidAgeError(Exception):
    pass

def get_user_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 150:
            raise InvalidAgeError("Invalid age! Age must be between 0 and 150.")
        else:
            print(f"Your age is: {age}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except InvalidAgeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_user_age()
