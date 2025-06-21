""" 
Practice Exercises
Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information.
"""
#class creation
class Student:

    #class initialization
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def display_student_information (self):
        return f"Name of student is {self.name} and age of student is {self.age}"

#object creation    
Student1 = Student("Samuel", 20)

#accessing and using functions from inside the Student Class
print(Student1.display_student_information())
print(type(Student1.age))

"""
Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.
"""
#class creation
class Product:

    #class initialization
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_stock_value(self):
        total_stock_value = self.price * self.quantity
        return f"Total Stock Value for {self.name} is Ghc {total_stock_value}"

Laptops = Product("Dell", 15000, 20)
Shoes = Product("Dessert", 1500, 15)
Fruits = Product("Orange", 50, 33)

laptop_total_stock_value = Laptops.total_stock_value()
shoe_total_stock_value = Shoes.total_stock_value()
fruit_total_stock_value = Fruits.total_stock_value()

print(laptop_total_stock_value)
print(shoe_total_stock_value)
print(fruit_total_stock_value)


#-----Added from work PC--------------------------
""" 
Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.
"""
class ValueTooHighError (Exception):
    def __init__(self, exception_caught):
        self.exception_caught = exception_caught

        