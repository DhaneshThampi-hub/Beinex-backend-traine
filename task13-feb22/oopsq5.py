'''5) Create a class named Student with name, score as instance attributes. Assign values to both of these attributes using a constructor.
Create 2 Student objects. And also define a method called 'display' in the Student class - which, when called should print the name and score of the student.
'''


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
student1 = Student(name="Alice", score=85)
student2 = Student(name="Bob", score=92)


student1.display()
print('\n')
student2.display()
