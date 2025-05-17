# 📘 OOP Assignments in Python

This repository contains a comprehensive set of Python Object-Oriented Programming (OOP) assignments covering fundamental and advanced concepts. Each assignment demonstrates a specific OOP feature with clean, simple examples.

---

## 🧠 Topics Covered

### 1. Using `self`

**Assignment**:
Create a `Student` class with attributes `name` and `marks`. Initialize using `self` in a constructor and define a `display()` method.

---

### 2. Using `cls`

**Assignment**:
Create a `Counter` class that uses a class variable and a class method with `cls` to track the number of created objects.

---

### 3. Public Variables and Methods

**Assignment**:
Create a `Car` class with a public variable `brand` and a public method `start()`. Access both from outside the class.

---

### 4. Class Variables and Class Methods

**Assignment**:
Create a `Bank` class with a class variable `bank_name` and a class method `change_bank_name(cls, name)` to update the name across all instances.

---

### 5. Static Methods

**Assignment**:
Create a `MathUtils` class with a static method `add(a, b)` that returns the sum. No instance or class variables used.

---

### 6. Constructors and Destructors

**Assignment**:
Create a `Logger` class that prints a message when an object is created (constructor) and destroyed (destructor).

---

### 7. Access Modifiers: Public, Protected, Private

**Assignment**:
Create an `Employee` class with:

* a public variable `name`
* a protected variable `_salary`
* a private variable `__ssn`

Access and observe their behavior from outside the class.

---

### 8. The `super()` Function

**Assignment**:
Create a `Person` class and a `Teacher` class that inherits from it. Use `super()` to call the base constructor in the derived class.

---

### 9. Abstract Classes and Methods

**Assignment**:
Use the `abc` module to define an abstract class `Shape` with an abstract method `area()`. Implement it in a `Rectangle` class.

---

### 10. Instance Methods

**Assignment**:
Create a `Dog` class with `name` and `breed`. Add an instance method `bark()` that prints a message using the dog's name.

---

### 11. Class Methods

**Assignment**:
Create a `Book` class with a class variable `total_books`. Add a class method `increment_book_count()` to update the count.

---

### 12. Static Methods

**Assignment**:
Create a `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)`.

---

### 13. Composition

**Assignment**:
Create `Engine` and `Car` classes. Use composition by passing an `Engine` object into the `Car` during initialization and access engine methods via the `Car`.

---

### 14. Aggregation

**Assignment**:
Create `Department` and `Employee` classes. Store an `Employee` reference in a `Department` object, where the `Employee` exists independently.

---

### 15. Method Resolution Order (MRO) and Diamond Inheritance

**Assignment**:
Create classes A, B, C, and D where B and C inherit from A, and D inherits from both B and C. Override `show()` in B and C and observe MRO in D.

---

### 16. Function Decorators

**Assignment**:
Write a decorator `log_function_call` that prints a message before calling a function. Apply it to a function `say_hello()`.

---

### 17. Class Decorators

**Assignment**:
Create a class decorator `add_greeting` that adds a method `greet()` returning `"Hello from Decorator!"` to a class `Person`.

---

### 18. Property Decorators: `@property`, `@setter`, and `@deleter`

**Assignment**:
Create a `Product` class with a private `_price` attribute. Use:

* `@property` to get the price
* `@price.setter` to update it
* `@price.deleter` to delete it

---

### 19. `callable()` and `__call__()`

**Assignment**:
Create a `Multiplier` class with a `__call__()` method that multiplies input by a stored factor. Use `callable()` to check if the object is callable.

---

### 20. Custom Exceptions

**Assignment**:
Define a custom exception `InvalidAgeError`. Create a function `check_age(age)` that raises it if age < 18 and handle it using `try...except`.

---

### 21. Custom Iterable Class

**Assignment**:
Create a `Countdown` class that implements `__iter__()` and `__next__()` so it can be used in a `for` loop to count down to 0.

---

## 🧪 How to Run

Ensure you have Python 3 installed. Clone the repo and run individual Python files:

```bash
python assignment_name.py
```

---

## 📚 Learning Objective

This set of assignments helps solidify your understanding of key OOP principles in Python, including:

* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Decorators
* Class vs instance behavior
* Advanced concepts like MRO, aggregation, composition, and custom iterables

---

## 👨‍💻 Author

**Taha Saif**
Student | Python Assignment | GIAIC Q3
