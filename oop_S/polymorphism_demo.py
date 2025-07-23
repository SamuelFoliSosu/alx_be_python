"""

2. Exploring Polymorphism and Method Overriding
mandatory
Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

Task Description:
You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:
Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
main.py (Provided for Testing):
This script demonstrates polymorphism by creating instances of Rectangle and Circle, invoking their area() method, and showing that each class calculates the area according to its shape.

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
Expected Output:
When you run main.py, the output should reflect the areas of the different shapes, showcasing polymorphism through method overriding.

The area of the Rectangle is: 50
The area of the Circle is: 153.93804002589985
Note for you:
Ensure your derived classes Rectangle and Circle correctly override the area method from the Shape base class. This is key to demonstrating polymorphism.
The NotImplementedError in the base area method serves as a reminder that this method is expected to be overridden in any subclass of Shape.
Through this task, you’ll see how different objects can be treated uniformly, yet behave differently based on their respective class implementations—a core concept of polymorphism.

"""
