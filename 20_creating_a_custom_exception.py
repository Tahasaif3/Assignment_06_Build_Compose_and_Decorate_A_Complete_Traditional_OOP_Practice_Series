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
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("No exceptions occurred.")