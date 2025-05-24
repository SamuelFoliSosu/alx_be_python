"""
Objective: Apply basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.

Task Description:

Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
Instructions:

Create a file named simple_interest.py.
Define three variables in this file:
principal with a value of 1000 (representing $1000),
rate with a value of 0.05 (representing 5% annual interest rate),
time with a value of 3 (representing 3 years).
Calculate the simple interest using the formula provided and store the result in a variable named interest.
Print the calculated interest in a format: The simple interest is: [interest].
Expected Output:

When executed, your script should print the simple interest calculated with the provided values. For principal = 1000, rate = 0.05, and time = 3, the output should be:

The simple interest is: 150.0

"""

#variable declarations
principal = 1000
rate = 0.05
time = 3

#simple interest calculation, results to 'interest' variable
interest = principal * rate * time

#printing results, ie . interest
print("The simple interest is: ",interest)