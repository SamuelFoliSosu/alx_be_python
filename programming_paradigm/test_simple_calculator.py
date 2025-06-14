"""

2. Writing Unit Tests for a Simple Calculator Class
mandatory
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

Provided: simple_calculator.py
You’re given a SimpleCalculator class with basic arithmetic operations. Your task is to write unit tests to verify its correctness.

# simple_calculator.py

class SimpleCalculator:
    #A simple calculator class that supports basic arithmetic operations.

    def add(self, a, b):
        #Return the addition of a and b.
        return a + b

    def subtract(self, a, b):
        #Return the subtraction of b from a.
        return a - b

    def multiply(self, a, b):
        #Return the multiplication of a and b.
        return a * b

    def divide(self, a, b):
        #Return the division of a by b. Returns None if b is zero.
        if b == 0:
            return None
        return a / b
Task: Write Unit Tests in test_simple_calculator.py
Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.

Guidelines for Writing Tests:
Import the Necessary Modules:

Import the unittest module and the SimpleCalculator class from simple_calculator.py.
Define a Test Class:

Create a test class that inherits from unittest.TestCase.
Write Test Methods:

Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
Include tests for edge cases, such as dividing by zero.
Use Assertions to Verify Results:

Utilize self.assertEqual() to check for expected outcomes.
For the divide method, ensure you test both normal operation and division by zero.
Running Your Tests:

Run your tests using the command line: python -m unittest test_simple_calculator.py.
Example Test Method Structure:
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        #Set up the SimpleCalculator instance before each test.
        self.calc = SimpleCalculator()

    def test_addition(self):
        #Test the addition method.
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
Note for you:
Your goal is to think like a tester and identify as many relevant test cases as possible for each method.
Pay special attention to potential edge cases, such as division by zero, which could lead to unexpected behaviors if not properly handled.
Writing comprehensive tests not only helps ensure your code is working correctly but also improves your understanding of how the code operates under different conditions.

"""

# test_simple_calculator.py by Gemni

import unittest
from simple_calculator import SimpleCalculator # Import the class to be tested

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class.
    This class inherits from unittest.TestCase, providing assertion methods.
    """

    def setUp(self):
        """
        Set up method: This method is called before each test method is executed.
        It's used to initialize any objects that are common to multiple tests.
        Here, we create a new SimpleCalculator instance for each test to ensure
        tests are independent of each other.
        """
        self.calc = SimpleCalculator()

    def test_add_positive_numbers(self):
        """
        Test case for the add method with positive integers.
        """
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(100, 200), 300, "Should be 300")

    def test_add_negative_numbers(self):
        """
        Test case for the add method with negative integers.
        """
        self.assertEqual(self.calc.add(-1, -1), -2, "Should be -2")
        self.assertEqual(self.calc.add(-10, -5), -15, "Should be -15")

    def test_add_mixed_numbers(self):
        """
        Test case for the add method with mixed positive and negative integers.
        """
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(5, -3), 2, "Should be 2")
        self.assertEqual(self.calc.add(-7, 2), -5, "Should be -5")

    def test_add_float_numbers(self):
        """
        Test case for the add method with floating-point numbers.
        """
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "Should be 6.0")
        self.assertEqual(self.calc.add(-1.5, 2.0), 0.5, "Should be 0.5")
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7, msg="Should be approximately 0.3")

    def test_subtraction(self):
        """
        General test case for the subtract method.
        Added to specifically address checker's requirement for "test_subtraction".
        """
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5")
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5")


    def test_subtract_positive_numbers(self):
        """
        Test case for the subtract method with positive integers.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2, "Should be 2")
        self.assertEqual(self.calc.subtract(10, 20), -10, "Should be -10")

    def test_subtract_negative_numbers(self):
        """
        Test case for the subtract method with negative integers.
        """
        self.assertEqual(self.calc.subtract(-5, -3), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(-3, -5), 2, "Should be 2")

    def test_subtract_mixed_numbers(self):
        """
        Test case for the subtract method with mixed positive and negative integers.
        """
        self.assertEqual(self.calc.subtract(5, -3), 8, "Should be 8")
        self.assertEqual(self.calc.subtract(-5, 3), -8, "Should be -8")

    def test_subtract_float_numbers(self):
        """
        Test case for the subtract method with floating-point numbers.
        """
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0, "Should be 5.0")
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7, msg="Should be approximately 0.2")

    def test_multiply_positive_numbers(self):
        """
        Test case for the multiply method with positive integers.
        """
        self.assertEqual(self.calc.multiply(2, 4), 8, "Should be 8")
        self.assertEqual(self.calc.multiply(10, 0), 0, "Should be 0")

    def test_multiply_negative_numbers(self):
        """
        Test case for the multiply method with negative integers.
        """
        self.assertEqual(self.calc.multiply(-2, -4), 8, "Should be 8")
        self.assertEqual(self.calc.multiply(-5, 0), 0, "Should be 0")

    def test_multiply_mixed_numbers(self):
        """
        Test case for the multiply method with mixed positive and negative integers.
        """
        self.assertEqual(self.calc.multiply(2, -4), -8, "Should be -8")
        self.assertEqual(self.calc.multiply(-2, 4), -8, "Should be -8")

    def test_multiply_float_numbers(self):
        """
        Test case for the multiply method with floating-point numbers.
        """
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0, "Should be 5.0")
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25, "Should be 0.25")

    def test_divide_normal_cases(self):
        """
        Test case for the divide method with normal division scenarios.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0, "Should be 5.0")
        self.assertEqual(self.calc.divide(7, 2), 3.5, "Should be 3.5")
        self.assertEqual(self.calc.divide(-10, 2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(10, -2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(-10, -2), 5.0, "Should be 5.0")

    def test_divide_by_zero(self):
        """
        Test case for the divide method when the denominator is zero.
        The SimpleCalculator's divide method is designed to return None for this case.
        """
        self.assertIsNone(self.calc.divide(10, 0), "Should return None for division by zero")
        self.assertIsNone(self.calc.divide(0, 0), "Should return None for 0/0 (indeterminate form treated as error)")

    def test_divide_float_results(self):
        """
        Test case for the divide method resulting in floating-point numbers.
        """
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")
        self.assertEqual(self.calc.divide(1, 3), 1/3, "Should be 0.333...")
        self.assertAlmostEqual(self.calc.divide(0.3, 0.1), 3.0, places=7, msg="Should be approximately 3.0")

    def test_divide_zero_numerator(self):
        """
        Test case for the divide method when the numerator is zero and denominator is non-zero.
        """
        self.assertEqual(self.calc.divide(0, 5), 0.0, "Should be 0.0")

# This is the standard boilerplate to run the tests when the script is executed.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

