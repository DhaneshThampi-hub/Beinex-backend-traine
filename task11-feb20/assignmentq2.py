'''2)Write a program to check the validity of a password. Primary conditions for password validation:
- minimum 8 charecters
- The alphabet must be between [a-z]
- At least one alphabet should be of Upper Case [A-Z]
- At least 1 number or digit between [0-9].
- At least 1 character from [ _ or @ or $ ]'''

def valid_password(password):
    if len(password) < 8:
        return False
    has_lowercase = False
    has_uppercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True 
    if not (has_lowercase and has_uppercase):
        return False
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False
    special_chars = ['_', '@', '$']
    special_char = any(char in special_chars for char in password)
    if not special_char:
        return False
    return True
password = input("Enter a password: ")
if valid_password(password):
    print("Valid password!")
else:
    print("Invalid password. Please follow the specified rules.")


