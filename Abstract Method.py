from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass   # abstract method — no body, must be defined in child class

# Derived class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # overriding abstract method
        return 3.14 * self.radius * self.radius

# Derived class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):   # overriding abstract method
        return self.length * self.width


c = Circle(5)
r = Rectangle(4, 6)

print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())
