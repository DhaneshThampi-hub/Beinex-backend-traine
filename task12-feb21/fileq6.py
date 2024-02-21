'''•	Write a Python program to read a random line from a file.'''

import random

def random_line(file_name):
        with open(file_name, 'r') as file:
            lines = file.read().splitlines()
            return random.choice(lines)
file_name = input('enter a file name: ')
random_text = random_line(file_name)
if random_text:
    print("Random line from the file:")
    print(random_text)
