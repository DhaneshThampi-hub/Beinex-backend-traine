'''17.Python program to delay printing of line from a file using sleep function'''

import time

def delay_print_from_file(file_path, delay_time):
    try:
        with open(file_path, 'r') as file:
            # Read each line from the file
            for line in file:
                # Print the line and introduce a delay
                print(line.strip())
                time.sleep(delay_time)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
file_path = 'file.txt'
delay_time = 2  # Specify the delay time in seconds

delay_print_from_file(file_path, delay_time)
