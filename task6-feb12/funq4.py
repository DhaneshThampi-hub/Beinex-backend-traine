'''4.	Write a Python program to reverse a string'''

def reverse_string(input_string):
    reversed_str = " "
    for i in range(len(input_string) - 1, -1, -1):
        reversed_str += input_string[i]
    return reversed_str
input = input("Enter a string: ")
reversed_string = reverse_string(input)
print("Reversed string:", reversed_string)