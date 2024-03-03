"""18.Python program to for student height record for a school using Class and 
Objects.
"""


class Student:
    def __init__(self, name, height):
        # Initialize the Student object with a name and height
        self.name = name
        self.height = height


class SchoolHeightRecord:
    def __init__(self):
        # Initialize the SchoolHeightRecord object with an empty list of students
        self.students = []

    def add_student(self, student):
        # Method to add a student to the record
        self.students.append(student)

    def display_records(self):
        # Method to display all student height records
        if not self.students:
            print("No records found.")
        else:
            print("Student Height Records:")
            for student in self.students:
                print(f"{student.name}: {student.height} cm")

    def find_tallest_student(self):
        # Method to find the tallest student in the record
        if not self.students:
            return None
        tallest_student = max(self.students, key=lambda x: x.height)
        return tallest_student

    def find_shortest_student(self):
        # Method to find the shortest student in the record
        if not self.students:
            return None
        shortest_student = min(self.students, key=lambda x: x.height)
        return shortest_student

    def calculate_average_height(self):
        # Method to calculate the average height of all students
        if not self.students:
            return None
        total_height = sum(student.height for student in self.students)
        average_height = total_height / len(self.students)
        return average_height

    def display_sorted_records(self):
        # Method to display student height records sorted by height in descending order
        if not self.students:
            print("No records found.")
        else:
            sorted_students = sorted(
                self.students, key=lambda x: x.height, reverse=True
            )
            print("Sorted Student Height Records:")
            for student in sorted_students:
                print(f"{student.name}: {student.height} cm")


# Example usage:
school_records = SchoolHeightRecord()

# Adding students to the record based on user input
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    student_name = input("Enter student name: ")
    student_height = float(input("Enter student height (in cm): "))
    student = Student(student_name, student_height)
    school_records.add_student(student)

# Displaying student height records
school_records.display_records()

# Finding the tallest and shortest students
tallest_student = school_records.find_tallest_student()
shortest_student = school_records.find_shortest_student()

if tallest_student:
    print(f"Tallest Student: {tallest_student.name} ({tallest_student.height} cm)")

if shortest_student:
    print(f"Shortest Student: {shortest_student.name} ({shortest_student.height} cm)")

# Calculating and displaying average height
average_height = school_records.calculate_average_height()
if average_height:
    print(f"Average Height of Students: {average_height:.2f} cm")

# Displaying sorted student height records
school_records.display_sorted_records()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
