# Assignment 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

#1. Using self Assignment

"""
Assignment:
Create a class Student with attributes name and marks.
Use the self keyword to initialize these values via a constructor.
Add a method display() that prints student details.
"""

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display_data(self):
        print(f"Name: {self.name} Marks: {self.marks}")

# Creating an object of the Student class
student1 = Student("Taha", 99)
student1.display_data()

#2. Using cls Assignment

"""
Assignment:
Create a class Counter that keeps track of how many objects have been created. 
Use a class variable and a class method with cls to manage and display the count.
"""

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Creating objects of the Counter class
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
Counter.display_count()


#3. Public Variables and Methods Assignment

"""
Assignment:
Create a class Car with a public variable brand and a public method start().
Instantiate the class and access both from outside the class
"""

class Car:
    def __init__(self,brand):
        self.brand = brand
    

    def start(self):
        print(f"{self.brand} is starting.")

my_car = Car("Toyota")
my_car.start()


#4. Class Variables and Class Methods

"""
Assignment:
Create a class Bank with a class variable bank_name.
Add a class method change_bank_name(cls, name) that
allows changing the bank name. Show that it affects
all instances of the class.
"""
    
class Bank:
    bank_name = "HBL Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}")

    def display_bank_name(self):
        print(f"Bank name is: {self.bank_name}")

    
# Creating objects of the Bank class
bank1 = Bank()
bank2 = Bank()
bank1.display_bank_name()
bank2.display_bank_name()

# Changing the bank name using class method
Bank.change_bank_name("Al Baraka Bank")
bank1.display_bank_name()
bank2.display_bank_name()

#5. Static Variables and Static Methods
"""
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum.
No class or instance variables should be used.
"""

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
    
# Using the static method
result = MathUtils.add(5, 10)
print(f"The sum is: {result}")


#6. Constructors and Destructors
"""
Assignment:
Create a class Logger that prints a message when an object is created (constructor)
and another message when it is destroyed (destructor).
"""

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

    
# Creating and deleting a Logger object
logger = Logger()
del logger


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
# Access public
print(employee.name)  #Public variable can be accessed
# Access protected
print(employee._salary) #Works but warning: "50000"
# Access private
# print(employee.__ssn) #Error: AttributeError
        
#8. The super() Function
"""
Assignment:
Create a class Person with a constructor that sets the name.
Inherit a class Teacher from it, add a subject field, and use
super() to call the base class constructor.
"""

class Person:
    def __init__(self,name):
        self.name = name

    
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Creating an object of the Teacher class
teacher = Teacher("Taha Saif", "Mathematics")
teacher.display_info()

#9. Abstract Classes and Methods
"""
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area().
Inherit a class Rectangle that implements area().
"""

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        print(f"Area of Rectangle: {self.area()}")

    def area(self):
        return self.length * self.width
    

# Creating an object of the Rectangle class
rectangle = Rectangle(5,10)

#10. Instance Methods
"""
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method
bark() that prints a message including the dog's name.
"""

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

    
# Creating an object of the Dog class  
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

#11. Class Methods
"""
Assignment:
Create a class Book with a class variable total_books. Add a class method 
increment_book_count() to increase the count when a new book is added.
"""

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

    
# Adding books
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

#12. Static Methods
"""
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c)
that returns the Fahrenheit value.
"""

class TemperatureConverter:
    @staticmethod
    def celsius_to_farenheit(celsius):
        return (celsius * 9/5) + 32
    

# Using the static method
temp = TemperatureConverter.celsius_to_farenheit(25)
print(f"Temperature in Fahrenheit: {temp}")

#13. Composition
"""
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object
to the Car class during initialization. Access a method of the Engine class via the
Car class.
"""

class Engine:
    def start(self):
        print("Engine started")

    
class Car:
    def __init__(self,engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()
        print("Car started")

    
# Creating an Engine object 
engine = Engine()
# Creating a Car object with the Engine object
car = Car(engine)
car.start_car()


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

# 15. Method Resolution Order (MRO) and Diamond Inheritance
"""
Assignment:
Create four classes:
A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.
Create an object of D and call show() to observe MRO.
"""

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  
    pass

obj = D()
obj.show()

print(D.__mro__)


#16. Function Decorators
"""
Assignment:
Write a decorator function log_function_call that prints "Function is being called"
before a function executes. Apply it to a function say_hello().
"""

def log_function_call(func):
    def wrapper(*args,**kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")


# Calling the function
say_hello("Taha")

#17. Class Decorators
"""
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet()
method returning "Hello from Decorator!". Apply it to a class Person.
"""

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self,name):
        self.name = name


    def display_name(self):
     return f"Name: {self.name}"

    
# Creating an object of the Person class
person = Person("Taha")
# Calling the greet method
print(person.greet())
# Calling the display_name method
print(person.display_name())

#18. Property Decorators: @property, @setter, and @deleter
"""
Assignment:
Create a class Product with a private attribute _price. Use @property to get the 
price, @price.setter to update it, and @price.deleter to delete it.
"""

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price
        print("Price deleted")


product = Product(100)
# Accessing the price using the property method
print(product.price)  # 100
# Updating the price using the setter method
product.price = 150
print(product.price)  # 150
# Deleting the price using the deleter method
product.price  # Price deleted
# print(product.price) 

# 19. callable() and __call__()
"""
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__()
method that multiplies an input by the factor. Test it with callable() and by 
calling the object like a function.
"""

class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    
    def __call__(self, value):
        return value * self.factor
    

multiplier = Multiplier(3)
print(callable(multiplier))  
result = multiplier(5)
print(f"Result: {result}")  

# 20. Creating a Custom Exception
"""
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that
raises this exception if age < 18. Handle it with try...except.
"""

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Age is valid.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
else:
    print("No exceptions occurred.")

# 21. Make a Custom Class Iterable
"""
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and 
__next__() to make the object iterable in a for-loop, counting down to 0.
"""

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current
    

# using the countdown class
countdown = Countdown(5)
for number in countdown:
    print(number)