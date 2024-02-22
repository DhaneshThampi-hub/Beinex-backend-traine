'''6) Extend the above solution and add another instance attribute called grade (should be string). Assign value to grade from within the constructor.
The value should not be taken from user input.
Instead use the following conditions and assign values to grade by using the value of score.
grade = A+ if score >=90
grade = A if score >=80 and <90
grade = B+ if score >=70 and <80
and so on.
if score is below 40 then grade should be "FAILED"
'''

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 90:
            return "A+"
        elif 80 <= self.score < 90:
            return "A"
        elif 70 <= self.score < 80:
            return "B+"
        elif 60 <= self.score < 70:
            return "B"
        elif 50 <= self.score < 60:
            return "C"
        else:
            return "FAILED"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.grade}")


student1 = Student(name="Ali", score=85)
student2 = Student(name="Balu", score=92)
student3=  Student(name="Dennis",score=30)
print("Student 1: ")
student1.display()
print("\nStudent 2: ")
student2.display()
print("\nStudent 3: ")
student3.display()
