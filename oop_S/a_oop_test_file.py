# Practice Exercises
# Exercise 1: Creating a Student Class
# Instructions:
# Define a Student class with attributes like name and age. Include a method to display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_name(self):
        """get name of student"""
        return self.name
    
    def get_student_age(self):
        """get age of student"""
        return self.age
    
    def display_student_info(self):
        """display information of student"""
        student_info = f"Student name: {self.name}, age: {self.age}"
        return student_info

Student1 = Student("Samuel",5)
print(Student1.name)
print(Student1.age)
print(Student1.get_student_age())
print(Student1.get_student_name())
print(Student1.display_student_info())

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

def login(email, password):
    # if email == "doe@alxafrica.com" and password == "vkdn343":
    #     return True
    # else:
    #     return False

    # return True if email == "doe@alxafrica.com" and password == "vkdn343" else False
    
    return email == "doe@alxafrica.com" and password == "vkdn3431"

print(login("doe@alxafrica.com","vkdn343"))

try:
    # code
    print("Hello Try")
except Exception:
    # code
    print("Hello Exception")
else:
    # code
    print("Hello Else")
finally:
    # code
    print("Hello Finally")

def divide(x , y):
    """divides two numbers, x as the numerator and y as the denomenator"""
    if y == 0:
        raise ZeroDivisionError("Division by zero is not alloweddddddd!")
    return x / y

# x = int(input("enter x value: "))
# y = int(input("enter y value: "))

print(divide(1 , 2))

class OutOfStockError(Exception):
    
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

#Sample Product Inventory
product_inventory = {
    "apple" : 10,
    "bannaa" : 5,
    "orange" : 0, #Out of stock
    "grapes" : 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] < quantity and product_inventory[item] != 0:
            print(f"{quantity} not possible, only {product_inventory[item]} {item}(s) left")
        elif product_inventory[item] < quantity and product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] = product_inventory[item] - quantity
            print(f"{product_inventory[item]} {item}(s) left")
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    # for p in range(11):
        purchase_item("apple" , 1)
        purchase_item("apple" , 3)
        purchase_item("orange" , 1)
        purchase_item("watermelon" , 1)
except OutOfStockError as e:
    print(e)