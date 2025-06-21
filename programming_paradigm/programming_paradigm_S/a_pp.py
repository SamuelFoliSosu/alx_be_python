""" 
Practice Exercises
Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information.
"""
print("\nFundamentals of OOP in Python \nExercise 1 -------------------------")

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

#-----------------------------------------------------------------------------------------------
"""
Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.
"""
print("\nFundamentals of OOP in Python \nExercise 2 -------------------------")

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

Dell_Laptops = Product("Dell", 15000, 20)
Dessert_Shoes = Product("Dessert", 1500, 15)
Orange_Fruits = Product("Orange", 50, 33)

dell_laptop_total_stock_value = Dell_Laptops.total_stock_value()
dessert_shoe_total_stock_value = Dessert_Shoes.total_stock_value()
orange_fruit_total_stock_value = Orange_Fruits.total_stock_value()

print(dell_laptop_total_stock_value)
print(dessert_shoe_total_stock_value)
print(orange_fruit_total_stock_value)
#-----------------------------------------------------------------------------------------------
"""
Exercise 1: Handling ZeroDivisionError

Instructions:

Write a program that takes two numbers as input from the user and divides the first number by the second number.
Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
"""
print("\nErrors and Exception Handling in Python \nExercise 1 -------------------------")

num1 = 5 #int(input("Enter first number to divid: "))
num2 = 0 #int(input("Enter second number to divide: "))

try:
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed, ow!")
except ZeroDivisionError as e:
    print(e)
else:
    print(num1 / num2)
finally:
    print("Printing finally block!")
#-----------------------------------------------------------------------------------------------
"""
Exercise 2: File Handling with FileNotFoundError

Instructions:

Write a program that attempts to open and read data from a file specified by the user.
Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.
"""
print("\nErrors and Exception Handling in Python \nExercise 2 -------------------------")

try:
    file = open('test_file.txt')
    if file.name != 'test_file.txt':
        raise FileNotFoundError('File not found or does not exist')
except FileNotFoundError as e:
    print(e)
else:
    print("#--------file start----------#")
    print(file.read())
    file.close()
    print("#---------file end-----------#")
finally:
    print("Finally!")

#-----------------------------------------------------------------------------------------------
"""
Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.
"""
print("\nErrors and Exception Handling in Python \nExercise 3 -------------------------")

try:
    pass
except:
    pass
else:
    pass
finally:
    pass
#-----------------------------------------------------------------------------------------------