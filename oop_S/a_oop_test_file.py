# Practice Exercises
# Exercise 1: Creating a Student Class
# Instructions:
# Define a Student class with attributes like name and age. Include a method to display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_name(self):
        return self.name
    
    def get_student_age(self):
        return self.age
    
    def display_student_info(self):
        student_info = f"Student name: {self.name}, age: {self.age}"
        return student_info

Student1 = Student("Samuel",5)
print(Student1.name)
print(Student1.age)
print(Student1.get_student_age())
print(Student1.get_student_name())

# Exercise 2: Creating a Product Catalog
# Instruction:
# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_of_products(self):
        total_value = self.price * self.quantity
        return total_value
    
Mangoes = Product("Mangoes",5,500)
print(Mangoes.name)
print(Mangoes.price)
print(Mangoes.quantity)
print(Mangoes.total_value_of_products())