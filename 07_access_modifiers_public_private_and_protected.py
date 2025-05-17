#7. Access Modifiers: Public, Private, and Protected
"""
Assignment:
Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
"""

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


# Creating an object of the Employee class
employee = Employee("Taha Saif", 50000, "123-45-6789")
employee.display_info()
# Accessing public variable
print(employee.name)  #Public variable can be accessed
# Access protected variable
print(employee._salary) #Works but warning: "50000"
# Access private variable
# print(employee.__ssn) #Error: AttributeError