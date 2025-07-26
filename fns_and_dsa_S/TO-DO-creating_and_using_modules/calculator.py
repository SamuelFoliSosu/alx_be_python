# Practice Exercises
# Exercise 1: Creating and Using Modules
# Instructions:
# Create a custom Python module named calculator.py that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division).
# Create functions add, subtract, multiply, and divide in the calculator.py module.
# Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.

def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    if num2 == 0:
        return "Can not divide by " + str(num2)
    else:
        return num1 / num2