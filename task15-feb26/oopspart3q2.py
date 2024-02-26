"""Extend the above solution and find the average expense per employee.
The calculation must be dynamic, there should be no need for you to manually code each addition 
operations. This can be done by keeping track of the objects being created – in a list (But don’t
manually append the objects to a list, this must happen when the objects are being created)"""


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def update_salary(self, hours, rate=200):
        self.salary = hours * rate

    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Unsupported operand types for +: 'Employee' and 'str'")
        return self.salary + other.salary


class PartTimeEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rate = 150

    def update_salary(self, hours):
        super().update_salary(hours, self.rate)


class getEmployees:
    employees = []

    def __init__(self, Employee):
        self.employees.append(Employee)

    @classmethod
    def average_expense_per_employee(cls):
        total_expense = sum(Employee.salary for Employee in cls.employees)
        return total_expense / len(cls.employees)


e1 = Employee(name=input("enter employee 1 name: "))
e1.update_salary(hours=int(input("enter hours: ")))
e2 = Employee(name=input("enter employee 2 name: "))
e2.update_salary(hours=int(input("enter hours: ")))

p1 = PartTimeEmployee(name=input("enter partime 1 person name: "))
p1.update_salary(hours=int(input("enter hours: ")))
p2 = PartTimeEmployee(name=input("enter partime 2 person name: "))
p2.update_salary(hours=int(input("enter hours: ")))


print(e1)
print(e2)
print(p1)
print(p2)


employees = [e1, e2, p1, p2]
total_expense = sum(employee.salary for employee in employees)
print(f"\nTotal Salary Expense: ${total_expense}")


te1 = getEmployees(e1)
te2 = getEmployees(e2)
te3 = getEmployees(p1)
te4 = getEmployees(p2)


average_expense = getEmployees.average_expense_per_employee()
print("Average expense per employee:", average_expense)
