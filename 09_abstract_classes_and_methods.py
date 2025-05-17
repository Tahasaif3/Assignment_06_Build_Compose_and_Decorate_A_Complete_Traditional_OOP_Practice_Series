#9. Abstract Classes and Methods
"""
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area().
Inherit a class Rectangle that implements area().
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        print(f"Area of Rectangle: {self.area()}")

    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(6,10)
    
