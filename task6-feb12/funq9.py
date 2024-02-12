'''9.	Define a function that accepts roll number and returns whether the student is present or absent.'''

def attendence(roll):
    x = [3,4,15,26]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("Enter roll no:  ")) 
attendence(roll)