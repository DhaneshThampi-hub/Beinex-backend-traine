'''7) Extend the above solution again and add another instance method called 'as_dict'. The method should return a dictionary with the data of the student.
 It should contain 'name', 'score', 'grade', keys and their respective values.'''


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

    def as_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.grade
        }
student1 = Student(name="Abin", score=85)
student2 = Student(name="Bale", score=25)

print("Student 1:")
student1.display()
print("\nStudent 2:")
student2.display()

student1_dict = student1.as_dict()
student2_dict = student2.as_dict()

print("\nStudent 1 data as dictionary:")
print(student1_dict)

print("\nStudent 2 data as dictionary:")
print(student2_dict)
