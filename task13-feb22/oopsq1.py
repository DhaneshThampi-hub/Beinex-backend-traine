'''1)Write a program to create a class by name Students,
 and initialize attributes like name, age, and grade while creating an object.'''


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
name=input("enter a name:  ")
age=int(input("enter the age: "))
grade=input("enter the grade: ")
student1 = Student(name, age, grade)
print(f"Student 1: Name={student1.name}, Age={student1.age}, Grade={student1.grade}")

