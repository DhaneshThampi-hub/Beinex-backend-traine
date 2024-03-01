"""15.Copy odd lines of one file to another file in Python"""


def copy_odd_lines(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            # Read all lines from the input file
            lines = infile.readlines()

            # Write odd lines to the output file
            for i in range(0, len(lines), 2):
                outfile.write(lines[i])

        print("Odd lines copied successfully!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
input_file_path = "file.txt"
output_file_path = "output1.txt"

copy_odd_lines(input_file_path, output_file_path)
