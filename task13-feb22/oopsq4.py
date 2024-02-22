'''4) Write a program to create a child class Teacher that will inherit the properties from the parent class Staff.
    attributes need for staff : role,department, salary
    attributes need for teacher: name,age
    method in  staff : def print_details()

    output expected -
        Name:  Raj
        Age:  28
        Role: Teacher
        Department: Science
'''

class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def details(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        super().details()  

teacher = Teacher(name="Raj", age=28, role="Teacher", department="Science", salary=55000)
teacher.details()
