'''2)Write a program that prints the class name using its object.'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

name=input("enter a name:  ")
age=int(input("enter the age: "))
grade=input("enter the grade: ")
student1 = Student(name, age, grade)
print(f"Class name of student1: {student1.__class__.__name__}")

