#14. Aggregation
"""
Assignment:
Create a class Department and a class Employee. Use aggregation by having a 
Department object store a reference to an Employee object that exists independently
of it.
"""

class Department:
    def __init__(self,name):
        self.name = name
        self.employees = []

    
    def add_employee(self,employee):
        self.employees.append(employee)

    
    def display_employees(self):
        print(f"Employees in {self.name} Department:")
        for emp in self.employees:
            print(emp.name)

    
class Employee:
    def __init__(self,name):
        self.name = name

    
# Creating a Department object
department = Department("HR")
# Creating Employee objects    
employee1 = Employee("Taha")
employee2 = Employee("Ahad")
# Adding employees to the department
department.add_employee(employee1) 
department.add_employee(employee2)
# Displaying employees in the department
department.display_employees()